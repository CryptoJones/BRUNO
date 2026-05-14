# BRUNO — Limitations, Scope, and Use Guidance

Read this before deploying BRUNO in any operational context.

---

## What BRUNO Does

Given a fireground scenario, BRUNO provides tactical guidance, ICS structure recommendations, hazmat references, and rescue decision support across the full range of fire service operations — structural firefighting, vehicle extrication, wildland/WUI, hazmat, and Mayday/RIT operations.

## What BRUNO Does Not Do

- **BRUNO is not an Incident Commander.** It cannot replace the situational awareness, judgment, and authority of the officer on scene.
- **BRUNO does not know your building.** It has no access to pre-plans, occupancy data, construction type, or actual fireground conditions. All tactical recommendations must be filtered through what you can see and verify.
- **BRUNO does not know your resources.** Staffing levels, apparatus capabilities, mutual aid agreements, and water supply are not known to BRUNO unless you tell it.
- **BRUNO does not know your SOGs.** Department-specific standard operating guidelines always take precedence over BRUNO output.
- **BRUNO cannot declare a Mayday.** Only the member in distress or their officer does that.
- **BRUNO has a training data cutoff.** NFPA code editions, IFSTA curriculum updates, and new research on fire behavior may not be reflected.
- **BRUNO is not a substitute for NFPA compliance review.** Code compliance determinations require a qualified authority having jurisdiction (AHJ).

---

## Scope of Practice

BRUNO is designed to assist trained fire service personnel in:

- Tactical decision support during training scenarios and tabletop exercises
- ICS structure and span-of-control reference
- Hazmat identification and ERG reference
- Mayday/RIT procedure review
- NFPA code and IFSTA curriculum reference
- After-action review and training development

**In active fireground operations, BRUNO is a reference — not a command authority. The Incident Commander's judgment governs.**

---

## For Fire Chiefs Considering Deployment

Before deploying BRUNO operationally, your training division should:

- Conduct tabletop exercises using BRUNO and evaluate outputs against department SOGs
- Identify any outputs that conflict with local SOGs and document them
- Establish a written policy on when BRUNO may be consulted (training vs. operational)
- Train company officers that BRUNO supplements — it does not override — their judgment
- Review NFPA edition currency against current BRUNO training data

BRUNO is most valuable as a **training tool** and a **reference during low-urgency planning**. In high-tempo fireground operations, there is no time to query an AI — decisions must come from trained instinct and established SOGs.

---

## Known Limitations

| Area | Limitation |
|------|-----------|
| Situational awareness | BRUNO has no real-time data; it knows only what you tell it |
| Building data | No access to pre-plans, occupancy records, or construction type |
| Resource data | Staffing, apparatus, water supply unknown unless provided |
| NFPA currency | Reflects NFPA editions current as of training data cutoff |
| WUI/wildland | Less comprehensive than structural; consult NWCG resources for wildland operations |
| Hazmat | ERG-based; consult CHEMTREC and your hazmat team for complex incidents |
| Training size | Fine-tuned on a small dataset; highly unusual scenarios may degrade performance |

---

## Version and Training Data

| Field | Value |
|-------|-------|
| Base model | meta-llama/Llama-3.3-70B-Instruct |
| Fine-tune method | QLoRA (4-bit) |
| Adapter | [Ronin48LLC/bruno-lora-adapter](https://huggingface.co/Ronin48LLC/bruno-lora-adapter) |
| Training date | May 2026 |
| NFPA edition | Current as of training data cutoff |
| ERG edition | 2024 |

---

## Reporting Errors

If BRUNO produces tactically incorrect, dangerous, or misleading output:

- **GitHub:** [CryptoJones/BRUNO/issues](https://github.com/CryptoJones/BRUNO/issues)
- **Codeberg:** [Ronin48/BRUNO/issues](https://codeberg.org/Ronin48/BRUNO/issues)

For outputs that could cause injury or death if followed, flag them urgently. Include the scenario input, the output, and the correct tactical answer.
