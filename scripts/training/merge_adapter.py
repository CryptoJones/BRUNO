"""Merge BRUNO LoRA adapter into base model for full-weight inference."""

import argparse
from pathlib import Path

import torch
import yaml
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def load_config(config_path: str) -> dict:
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    cfg = load_config(args.config)
    base_model = cfg["model"]["base_model"]
    adapter_path = cfg["training"]["output_dir"]
    merged_path = cfg["merge"]["merged_model_path"]

    print(f"Loading base model: {base_model}")
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.bfloat16,
        device_map="cpu",
    )

    print(f"Loading adapter: {adapter_path}")
    model = PeftModel.from_pretrained(model, adapter_path)

    print("Merging adapter...")
    model = model.merge_and_unload()

    print(f"Saving merged model to {merged_path}")
    model.save_pretrained(merged_path)
    tokenizer.save_pretrained(merged_path)
    print("Done.")


if __name__ == "__main__":
    main()
