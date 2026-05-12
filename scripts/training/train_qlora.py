"""QLoRA fine-tuning script for BRUNO."""

import argparse
import json
from pathlib import Path

import torch
import yaml
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from trl import SFTTrainer

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def load_config(config_path: str) -> dict:
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_dataset(dataset_path: str) -> Dataset:
    records = []
    with open(dataset_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return Dataset.from_list(records)


def format_messages(example: dict, tokenizer) -> dict:
    text = tokenizer.apply_chat_template(
        example["messages"],
        tokenize=False,
        add_generation_prompt=False,
    )
    return {"text": text}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    cfg = load_config(args.config)
    model_cfg = cfg["model"]
    quant_cfg = cfg["quantization"]
    lora_cfg = cfg["lora"]
    train_cfg = cfg["training"]
    data_cfg = cfg["data"]

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=quant_cfg["load_in_4bit"],
        bnb_4bit_compute_dtype=getattr(torch, quant_cfg["bnb_4bit_compute_dtype"]),
        bnb_4bit_use_double_quant=quant_cfg["bnb_4bit_use_double_quant"],
        bnb_4bit_quant_type=quant_cfg["bnb_4bit_quant_type"],
    )

    tokenizer = AutoTokenizer.from_pretrained(model_cfg["base_model"])
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(
        model_cfg["base_model"],
        quantization_config=bnb_config,
        device_map=model_cfg["device_map"],
        torch_dtype=getattr(torch, model_cfg["torch_dtype"]),
    )
    model = prepare_model_for_kbit_training(model)

    peft_config = LoraConfig(
        r=lora_cfg["r"],
        lora_alpha=lora_cfg["lora_alpha"],
        target_modules=lora_cfg["target_modules"],
        lora_dropout=lora_cfg["lora_dropout"],
        bias=lora_cfg["bias"],
        task_type=lora_cfg["task_type"],
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    dataset = load_dataset(data_cfg["dataset_path"])
    dataset = dataset.map(lambda x: format_messages(x, tokenizer))
    split = dataset.train_test_split(test_size=1 - data_cfg["train_split"], seed=42)

    training_args = TrainingArguments(
        output_dir=train_cfg["output_dir"],
        num_train_epochs=train_cfg["num_train_epochs"],
        per_device_train_batch_size=train_cfg["per_device_train_batch_size"],
        gradient_accumulation_steps=train_cfg["gradient_accumulation_steps"],
        gradient_checkpointing=train_cfg["gradient_checkpointing"],
        optim=train_cfg["optim"],
        save_steps=train_cfg["save_steps"],
        logging_steps=train_cfg["logging_steps"],
        learning_rate=train_cfg["learning_rate"],
        weight_decay=train_cfg["weight_decay"],
        fp16=train_cfg["fp16"],
        bf16=train_cfg["bf16"],
        max_grad_norm=train_cfg["max_grad_norm"],
        warmup_ratio=train_cfg["warmup_ratio"],
        group_by_length=train_cfg["group_by_length"],
        lr_scheduler_type=train_cfg["lr_scheduler_type"],
        report_to=train_cfg["report_to"],
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=split["train"],
        eval_dataset=split["test"],
        peft_config=peft_config,
        dataset_text_field="text",
        max_seq_length=data_cfg["max_seq_length"],
        tokenizer=tokenizer,
        args=training_args,
    )

    trainer.train()
    trainer.save_model(train_cfg["output_dir"])
    print(f"Training complete. Model saved to {train_cfg['output_dir']}")


if __name__ == "__main__":
    main()
