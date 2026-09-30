# Competitive-programming training data catalog

I compiled the public Hugging Face datasets used to post-train competitive-programming models such as [DeepCoder-14B-Preview](https://huggingface.co/agentica-org/DeepCoder-14B-Preview) and [X-Coder](https://huggingface.co/IIGroup/X-Coder-RL-Qwen3-8B).

This repository is an index. The rows stay on Hugging Face. Click a dataset name for size, file count, and Hub links.

Machine-readable copy: [`catalog.json`](catalog.json). Sizes are the sum of files on Hugging Face `main` (2026-09-30).

## Objective

Fine-tune [`deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) for competitive programming.

**Final model:** [`agentica-org/DeepCoder-14B-Preview`](https://huggingface.co/agentica-org/DeepCoder-14B-Preview)

One stage: base → RLVR (GRPO / GRPO+) → DeepCoder

| Level | Training model | Training method | Training data | Objective |
| --- | --- | --- | --- | --- |
| L1 | [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | GRPO (GRPO+) | [DeepCoder-Preview-Dataset](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset) | [DeepCoder-14B-Preview](https://huggingface.co/agentica-org/DeepCoder-14B-Preview) |
| L2 | [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | GRPO (GRPO+) | pick or build from the RL table below | [DeepCoder-14B-Preview](https://huggingface.co/agentica-org/DeepCoder-14B-Preview) |
| L3 | [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | GRPO, SFT, or SFT then RL | pick or build from the RL and SFT tables | [DeepCoder-14B-Preview](https://huggingface.co/agentica-org/DeepCoder-14B-Preview) |

A cheaper fallback is the X-Coder 8B path: SFT on [`IIGroup/X-Coder-SFT-376k`](https://huggingface.co/datasets/IIGroup/X-Coder-SFT-376k), then GRPO on [`IIGroup/X-Coder-RL-40k`](https://huggingface.co/datasets/IIGroup/X-Coder-RL-40k).

## Default L1 mix

| Field | Value |
| --- | --- |
| Base | [`deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) |
| Method | GRPO (GRPO+) |
| Data | [`agentica-org/DeepCoder-Preview-Dataset`](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset) (24,287 train problems) |
| Target | [`agentica-org/DeepCoder-14B-Preview`](https://huggingface.co/agentica-org/DeepCoder-14B-Preview) |
| LiveCodeBench | 2024-08-01 to 2025-02-01, 279 problems |

## Reference recipes

| Work | Role | Base | Data | Method | LiveCodeBench |
| --- | --- | --- | --- | --- | --- |
| [DeepCoder-14B-Preview](https://huggingface.co/agentica-org/DeepCoder-14B-Preview) | **target** | DeepSeek-R1-Distill-Qwen-14B | DeepCoder-Preview-Dataset (24k) | GRPO+; train 16K → 32K | v5 window below; match the frozen generation-length column |
| [NousCoder-14B](https://huggingface.co/NousResearch/NousCoder-14B) | not adopted; see the note at the end | Qwen3-14B | DeepCoder 24k, then drop ~10k already-solved | DAPO (GRPO variant) | v6 40K 63.35; 80K + YaRN 67.87 |
| [X-Coder RL (Qwen3-8B)](https://huggingface.co/IIGroup/X-Coder-RL-Qwen3-8B) | compute fallback | X-Coder-SFT-Qwen3-8B | X-Coder-RL-40k | GRPO | v5 59.4 → 64.0; v6 55.4 → 56.5 |

DeepCoder vs its base on LiveCodeBench v5 (2024-08-01 to 2025-02-01), from the [model card](https://huggingface.co/agentica-org/DeepCoder-14B-Preview):

| Model | 16K | 32K | 64K |
| --- | ---: | ---: | ---: |
| DeepCoder-14B-Preview | 45.6 | 57.9 | 60.6 |
| DeepSeek-R1-Distill-Qwen-14B | 50.2 | 53.0 | 53.0 |

Zevo freezes `max_new_tokens` in the baseline round. Match the column for that length.

## LiveCodeBench window

DeepCoder train contains LiveCodeBench problems from **2023-05 to 2024-07**. The test window is **2024-08-01 to 2025-02-01**, **279 problems**. That is the row count of the `lcbv5` test split in [DeepCoder-Preview-Dataset](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset), and it matches the DeepCoder paper window. I have not checked problem-by-problem that these 279 rows are the paper's eval items.

Do not sample validation from 2023-05 to 2024-07. Any Codeforces-sourced mix (DeepCoder, open-r1/codeforces, rStar-Coder seeds) needs a date-based overlap check against this test window.

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
| [OpenCodeReasoning-2](datasets/nvidia--OpenCodeReasoning-2.md) | [46.02 GiB](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2/tree/main) | [131](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2/tree/main) | ~2.16M (Python ~1.42M · C++ ~742k) | CC BY 4.0 | [card](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2) |

The OpenCodeReasoning-2 Hugging Face viewer first-5GB slice is Python 120,000 · C++ 100,000. The Hub size API estimates the full set at 2,164,812 rows (Python 1,422,489 · C++ 742,323).

## Download

```bash
python3 scripts/download.py --list
python3 scripts/download.py agentica-org/DeepCoder-Preview-Dataset
```

`scripts/download.py` calls `huggingface_hub.snapshot_download` and writes under `data/`, which is gitignored. Install `huggingface_hub` first. File counts and byte sizes were taken from the Hugging Face tree API on 2026-09-30.

## License

The catalog, README, and download script in this repository are MIT. Each listed dataset keeps the license on its Hugging Face card. This repository does not grant rights to redistribute those rows.

## NousCoder-14B not adopted

NousCoder-14B was not adopted: it only published the trained model's scores at 40K (63.35) and 80K + YaRN (67.87). The base score 60.79 does not state the generation length, so it is not a confirmed same-condition comparison.
