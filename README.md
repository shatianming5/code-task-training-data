# Competitive-programming training data catalog

I compiled the public Hugging Face datasets used to post-train competitive-programming models such as [NousCoder-14B](https://huggingface.co/NousResearch/NousCoder-14B) and [X-Coder](https://huggingface.co/IIGroup/X-Coder-RL-Qwen3-8B).

This repository is an index. The rows stay on Hugging Face. Click a dataset name for size, file count, and Hub links.

Machine-readable copy: [`catalog.json`](catalog.json). Sizes are the sum of files on Hugging Face `main` (2026-09-30).

## Default L1 mix

| Field | Value |
| --- | --- |
| Base | [`Qwen/Qwen3-14B`](https://huggingface.co/Qwen/Qwen3-14B) |
| Method | GRPO / DAPO |
| Data | [`agentica-org/DeepCoder-Preview-Dataset`](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset) (24,287 train problems) |
| Target | [`NousResearch/NousCoder-14B`](https://huggingface.co/NousResearch/NousCoder-14B) |
| LiveCodeBench v6 | 60.79 → 63.35 at 40K context; 67.87 at 80K + YaRN |

A cheaper fallback is the X-Coder 8B path: SFT on [`IIGroup/X-Coder-SFT-376k`](https://huggingface.co/datasets/IIGroup/X-Coder-SFT-376k), then GRPO on [`IIGroup/X-Coder-RL-40k`](https://huggingface.co/datasets/IIGroup/X-Coder-RL-40k).

## LiveCodeBench window

DeepCoder train contains LiveCodeBench problems from **2023-05 to 2024-07**. Use **2024-08-01 to 2025-05-01** (LiveCodeBench v6, 454 problems) as the test window. Do not sample validation from the earlier window.

Any Codeforces-sourced mix (DeepCoder, open-r1/codeforces, rStar-Coder seeds) needs a date-based overlap check against that test window.

## RL data (problems with tests)

| Dataset | Size | Files | Rows | License | Hugging Face |
| --- | ---: | ---: | ---: | --- | --- |
| [DeepCoder-Preview-Dataset](datasets/agentica-org--DeepCoder-Preview-Dataset.md) | [7.28 GiB](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset/tree/main) | [31](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset/tree/main) | 24,287 train | MIT | [card](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset) |
| [RLVR_Coding_Problems](datasets/NousResearch--RLVR_Coding_Problems.md) | [8.69 GiB](https://huggingface.co/datasets/NousResearch/RLVR_Coding_Problems/tree/main) | [4](https://huggingface.co/datasets/NousResearch/RLVR_Coding_Problems/tree/main) | same as DeepCoder | Apache-2.0 | [card](https://huggingface.co/datasets/NousResearch/RLVR_Coding_Problems) |
| [X-Coder-RL-40k](datasets/IIGroup--X-Coder-RL-40k.md) | [16.76 GiB](https://huggingface.co/datasets/IIGroup/X-Coder-RL-40k/tree/main) | [12](https://huggingface.co/datasets/IIGroup/X-Coder-RL-40k/tree/main) | ~40,000 | Apache-2.0 | [card](https://huggingface.co/datasets/IIGroup/X-Coder-RL-40k) |
| [Skywork-OR1-RL-Data](datasets/Skywork--Skywork-OR1-RL-Data.md) (`code`) | [784.98 MiB](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data/tree/main) | [6](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data/tree/main) | 14,057 code | Unspecified | [card](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data) |
| [KlearReasoner-CodeSub-15K](datasets/Kwai-Klear--KlearReasoner-CodeSub-15K.md) | [3.88 GiB](https://huggingface.co/datasets/Kwai-Klear/KlearReasoner-CodeSub-15K/tree/main) | [3](https://huggingface.co/datasets/Kwai-Klear/KlearReasoner-CodeSub-15K/tree/main) | 15,001 | Apache-2.0 | [card](https://huggingface.co/datasets/Kwai-Klear/KlearReasoner-CodeSub-15K) |
| [rStar-Coder](datasets/microsoft--rStar-Coder.md) (`synthetic_rl`) | [440.29 GiB](https://huggingface.co/datasets/microsoft/rStar-Coder/tree/main) | [867](https://huggingface.co/datasets/microsoft/rStar-Coder/tree/main) | 398,107 RL | CC BY 4.0 | [card](https://huggingface.co/datasets/microsoft/rStar-Coder) |
| [open-r1/codeforces](datasets/open-r1--codeforces.md) (`verifiable`) | [227.09 GiB](https://huggingface.co/datasets/open-r1/codeforces/tree/main) | [2,219](https://huggingface.co/datasets/open-r1/codeforces/tree/main) | 8,338 verifiable train | ODC-By 4.0 | [card](https://huggingface.co/datasets/open-r1/codeforces) |
| [TACO-verified](datasets/likaixin--TACO-verified.md) | [1.79 GiB](https://huggingface.co/datasets/likaixin/TACO-verified/tree/main) | [3](https://huggingface.co/datasets/likaixin/TACO-verified/tree/main) | 12,898 | MIT | [card](https://huggingface.co/datasets/likaixin/TACO-verified) |
| [AReaL-boba-2-RL-Code](datasets/inclusionAI--AReaL-boba-2-RL-Code.md) | [10.46 GiB](https://huggingface.co/datasets/inclusionAI/AReaL-boba-2-RL-Code/tree/main) | [11](https://huggingface.co/datasets/inclusionAI/AReaL-boba-2-RL-Code/tree/main) | 554 | Apache-2.0 | [card](https://huggingface.co/datasets/inclusionAI/AReaL-boba-2-RL-Code) |

LiveCodeBench overlap: DeepCoder / RLVR contain 2023-05 to 2024-07 items (test only after 2024-08). Codeforces-seeded sets (open-r1, rStar) need a date check. X-Coder is synthetic. Skywork removed similar LiveCodeBench items without a date cutoff.

## SFT data (long traces)

| Dataset | Size | Files | Rows | License | Hugging Face |
| --- | ---: | ---: | ---: | --- | --- |
| [rStar-Coder](datasets/microsoft--rStar-Coder.md) (`synthetic_sft`, `seed_sft`) | [440.29 GiB](https://huggingface.co/datasets/microsoft/rStar-Coder/tree/main) | [867](https://huggingface.co/datasets/microsoft/rStar-Coder/tree/main) | 398,183 · 591,660 | CC BY 4.0 | [card](https://huggingface.co/datasets/microsoft/rStar-Coder) |
| [X-Coder-SFT-376k](datasets/IIGroup--X-Coder-SFT-376k.md) | [21.48 GiB](https://huggingface.co/datasets/IIGroup/X-Coder-SFT-376k/tree/main) | [123](https://huggingface.co/datasets/IIGroup/X-Coder-SFT-376k/tree/main) | 376,491 | MIT | [card](https://huggingface.co/datasets/IIGroup/X-Coder-SFT-376k) |
| [OpenCodeReasoning](datasets/nvidia--OpenCodeReasoning.md) | [9.06 GiB](https://huggingface.co/datasets/nvidia/OpenCodeReasoning/tree/main) | [42](https://huggingface.co/datasets/nvidia/OpenCodeReasoning/tree/main) | 567,850 · 167,405 | CC BY 4.0 | [card](https://huggingface.co/datasets/nvidia/OpenCodeReasoning) |
| [OpenCodeReasoning-2](datasets/nvidia--OpenCodeReasoning-2.md) | [46.02 GiB](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2/tree/main) | [131](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2/tree/main) | Python 120,000 · C++ 100,000 | CC BY 4.0 | [card](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2) |

## Download

```bash
python3 scripts/download.py --list
python3 scripts/download.py agentica-org/DeepCoder-Preview-Dataset
```

`scripts/download.py` calls `huggingface_hub.snapshot_download` and writes under `data/`, which is gitignored. Install `huggingface_hub` first. File counts and byte sizes were taken from the Hugging Face tree API on 2026-09-30.

## License

The catalog, README, and download script in this repository are MIT. Each listed dataset keeps the license on its Hugging Face card. This repository does not grant rights to redistribute those rows.
