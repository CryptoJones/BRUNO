# BRUNO — Building Rescue and Unified Navigation Operations

> *"There is no call too routine or too small to treat with complete respect."*
> — Chief Alan Brunacini, Phoenix Fire Department

**BRUNO** is an AI assistant fine-tuned on fire service operations, incident command, hazardous materials, structural firefighting tactics, and rescue operations — built to assist **Firefighters, Company Officers, and Incident Commanders** in the field and in training.

Named after **Chief Alan Brunacini** of the Phoenix Fire Department — the father of modern Incident Command, the architect of FIRESCOPE, and the man who put "Be Nice" on the back of a fire helmet.

Part of the **Ronin 48** suite alongside SELMA, BONES, ABBY, and ATTICUS.

---

## Supporters

BRUNO is community-funded. Every contribution keeps this project free, open, and in the hands of the companies who need it most.

| Donor | Amount | Note |
|---|---|---|
| Ronin 48, LLC | N/A | Founding donor & primary sponsor of research time and equipment |

*Want to support BRUNO? Reach out to the maintainers.*

---

## Overview

| Attribute | Value |
|---|---|
| **Full Name** | Building Rescue and Unified Navigation Operations |
| **Named After** | Chief Alan Brunacini, Phoenix Fire Department |
| **Role** | Fire service tactical decision support |
| **Users** | Firefighters, Company Officers, Incident Commanders |
| **Base Model** | `meta-llama/Llama-3.3-70B-Instruct` (fine-tuned) |
| **Baseline** | `meta-llama/Llama-3.3-70B-Instruct` (prompt-only) |
| **Suite** | Ronin 48 — Model #5 |

---

## Capabilities

- **Size-up** — Building construction types, occupancy hazards, life safety priorities, RECEO-VS framework
- **Incident Command** — ICS/NIMS structure, sector assignments, resource tracking, span of control
- **Structural firefighting** — Attack line placement, ventilation, search and rescue, RIT operations
- **Hazmat** — DOT placard identification, ERG lookups, decon procedures, hot/warm/cold zone setup
- **Extrication** — Vehicle stabilization, disentanglement techniques, tool selection, medical coordination
- **Water supply** — Hydrant calculations, relay pumping, tanker shuttle, rural water ops
- **Wildland/WUI** — LCES, fire behavior, structure triage, defensible space assessment
- **Special rescue** — Confined space, trench rescue, rope rescue, water rescue
- **Mayday/RIT** — LUNAR reporting, air management, thermal imaging, RIT deployment
- **Pre-fire planning** — Building walkthrough checklists, Knox box, FDC locations, occupant load

---

## Architecture

```
BRUNO
├── src/bruno/          Core library (prompts, model interface)
├── scripts/
│   ├── data_collection/    Protocol and guideline scrapers
│   ├── training/           QLoRA fine-tuning pipeline
│   └── evaluation/         Tactical accuracy benchmarks
├── configs/            Training and model configuration
├── data/
│   ├── raw/            Source documents and datasets
│   ├── processed/      Cleaned, formatted training data
│   └── synthetic/      AI-generated fireground scenarios
├── ollama/             Modelfile for local deployment
└── tests/              Unit tests
```

---

## Training Data Sources

| Source | Description | License |
|---|---|---|
| NFPA 1 / NFPA 101 / NFPA 13 | Fire code, life safety, suppression systems | Public reference |
| IFSTA Essentials / Fire Officer | Core curriculum for firefighter and officer training | Public guidelines |
| NIOSH Fire Fighter Fatality Reports | Line-of-duty death investigations | Public Domain |
| NIST Fire Research | Structural fire behavior research, UL studies | Public Domain |
| DOT Emergency Response Guidebook (ERG) | Hazardous materials emergency response | Public Domain |
| ICS-100 through ICS-400 | FEMA NIMS/ICS training materials | Public Domain |
| FEMA/USFA Fire Data | National fire statistics, incident data | Public Domain |
| Synthetic Scenarios | AI-generated fireground and incident scenarios | Proprietary |

---

## Quick Start

```bash
# Baseline (prompt-only, no fine-tuning required)
ollama run Ronin48/bruno:v0.1.0

# Fine-tuned (after training completes)
ollama run Ronin48/bruno:v1.0.0
```

---

## Training

```bash
# Generate synthetic scenarios
python scripts/data_collection/generate_synthetic.py

# Prepare dataset
python scripts/training/prepare_dataset.py

# Train (QLoRA on 70B)
python scripts/training/train_qlora.py --config configs/training_config.yaml

# Merge adapter
python scripts/training/merge_adapter.py --config configs/training_config.yaml
```

---

## Related Models — Ronin 48 First Responder Suite

BRUNO, BONES, and SELMA are the three first responder models. They share scenes constantly — consult the appropriate model for each domain.

| Model | Domain | Use When... |
|---|---|---|
| **BRUNO** | Fire Service — Company Officer / IC | Fireground tactics, size-up, hazmat, extrication, water supply, ICS |
| **[BONES](https://codeberg.org/Ronin48/BONES)** | EMS — EMR / EMT / AEMT / Paramedic | Patient assessment, treatment protocols, drug dosing, triage, transport |
| **[SELMA](https://codeberg.org/Ronin48/SELMA)** | Law Enforcement | Criminal statute identification, charge elements, constitutional flags |

### Common Shared Scenes

| Scene Type | Primary | Support |
|---|---|---|
| Structure fire with casualties | BRUNO (fireground ops) | BONES (patient care) |
| Vehicle accident with entrapment | BRUNO (extrication) | BONES (patient care during extrication) |
| Hazmat with patient exposures | BRUNO (mitigation, decon zone) | BONES (patient decon and treatment) |
| Mass casualty incident | BONES (triage, treatment) | BRUNO (ICS, sectors) + SELMA (criminal nexus if applicable) |
| Arson investigation | BRUNO (origin/cause, fire behavior) | SELMA (arson statutes) + BONES (patient care) |
| DUI crash with entrapment | BRUNO (extrication) | BONES (patient care) + SELMA (criminal charges) |
| Wildland/WUI with structure threat | BRUNO (tactical operations) | BONES (civilian casualties) |
| Active shooter / active threat | BRUNO (scene safety, ICS) | BONES (casualty care, TECC) + SELMA (legal authority) |
| Cardiac arrest in a burning structure | BRUNO (scene safety, egress) | BONES (resuscitation protocol) |
| Confined space rescue | BRUNO (rescue ops, atmospheric monitoring) | BONES (patient extraction and care) |

> ABBY (digital forensics) operates independently of the first responder suite. SELMA pairs with [ATTICUS](https://codeberg.org/Ronin48/ATTICUS) on the legal side — prosecution and defense counterparts.

---

## ⚠ Disclaimer

**BRUNO is a tactical decision support tool, not a replacement for your training, your officer, or your IC.**

- All tactical decisions must follow your department's SOGs, SOPs, and incident command.
- BRUNO does not replace Mayday procedures, air management, or RIT activation — follow your training.
- Hazmat recommendations must be verified against the current ERG and your local hazmat team.
- This tool is intended for training and reference only — it is not a substitute for live drills, NFPA certification, or medical direction on fire-related injuries.

**When in doubt, call your IC.**

---

## Training Notes

If you're training BRUNO on RunPod or another GPU cloud provider, read [LESSONS_LEARNED.md](LESSONS_LEARNED.md)
before you start. ABBY's file has the most complete record of first-run errors and fixes —
BRUNO's file links there and will capture any BRUNO-specific issues as they arise.

---

## License

MIT License — see [LICENSE](LICENSE)

---

Proudly Made in Nebraska. Go Big Red!
