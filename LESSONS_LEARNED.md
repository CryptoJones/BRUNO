# Lessons Learned — BRUNO Training

This document captures dependency conflicts, environment bugs, and hard-won fixes
encountered during BRUNO training runs. Read this before you start.

For issues common to all Ronin 48 models (RunPod environment, bitsandbytes, torchvision,
QLoRA dependency conflicts), see [ABBY's LESSONS_LEARNED.md](https://codeberg.org/Ronin48/ABBY/raw/branch/main/LESSONS_LEARNED.md) —
it has the most complete record of the first training run.

---

## BRUNO-Specific Notes

### Disk Requirements (Llama-3.3-70B)

BRUNO uses Llama-3.3-70B, same as BONES. **Minimum volume: 200 GB. Recommended: 300 GB.**
A 100 GB volume will fill at shard 22/30 during model download and crash training before
the GPU ever activates.

The training monitor has been updated with pre-flight disk checks to catch this before
wasting time and credits. See [ABBY Error #20](https://codeberg.org/Ronin48/ABBY/raw/branch/main/LESSONS_LEARNED.md)
for full details.

**Rule: `GPU 0% | active=False` after 20+ minutes = crashed. SSH in and check `/workspace/logs/train.log`.**

---

## Contributing

If you hit a new error and fix it, please add it here. The people walking behind
you will thank you.
