# Competitive-programming training data catalog

I compiled the public Hugging Face datasets used to post-train competitive-programming models such as [NousCoder-14B](https://huggingface.co/NousResearch/NousCoder-14B) and [X-Coder](https://huggingface.co/IIGroup/X-Coder-RL-Qwen3-8B).

This repository is an index. The rows stay on Hugging Face. rStar-Coder is over 480 GB, X-Coder-RL-40k is 18 GB, and GitHub is the wrong host for those files.

Machine-readable copy: [`catalog.json`](catalog.json).

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

| Dataset | License | Scale | Source | LiveCodeBench overlap |
| --- | --- | --- | --- | --- |
| [agentica-org/DeepCoder-Preview-Dataset](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset) | MIT | 24,287 train (primeintellect 16,252 · taco 7,436 · lcbv5 599) | TACO-Verified, SYNTHETIC-1, LiveCodeBench | Contains 2023-05 to 2024-07; test only after 2024-08 |
| [NousResearch/RLVR_Coding_Problems](https://huggingface.co/datasets/NousResearch/RLVR_Coding_Problems) | Apache-2.0 | 9.33 GB | Same problems, NousCoder format | Same as DeepCoder |
| [IIGroup/X-Coder-RL-40k](https://huggingface.co/datasets/IIGroup/X-Coder-RL-40k) | Apache-2.0 | ~40k, 18 GB | Fully synthetic | Low risk; card does not document decontamination |
| [Skywork/Skywork-OR1-RL-Data](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data) (`code`) | Unspecified | 14,057 | LeetCodeDataset, TACO | Similar LiveCodeBench items removed; no date cutoff |
| [Kwai-Klear/KlearReasoner-CodeSub-15K](https://huggingface.co/datasets/Kwai-Klear/KlearReasoner-CodeSub-15K) | Apache-2.0 | 15,001 | Cleaned rllm RL subset | Not documented |
| [microsoft/rStar-Coder](https://huggingface.co/datasets/microsoft/rStar-Coder) (`synthetic_rl`) | CC BY 4.0 | 398,107; all splits >480 GB | Synthetic, CodeChef/Codeforces seeds | Deduplicate Codeforces by date |
| [open-r1/codeforces](https://huggingface.co/datasets/open-r1/codeforces) (`verifiable`) | ODC-By 4.0 | 8,338 train | Codeforces | Deduplicate by contest date; skip the dataset test split |
| [likaixin/TACO-verified](https://huggingface.co/datasets/likaixin/TACO-verified) | MIT | 12,898 | TACO | Older problems; residual overlap is low |
| [inclusionAI/AReaL-boba-2-RL-Code](https://huggingface.co/datasets/inclusionAI/AReaL-boba-2-RL-Code) | Apache-2.0 | 554, 11.2 GB | Unspecified | Not documented |

## SFT data (long traces)

| Dataset | License | Scale | Source |
| --- | --- | --- | --- |
| [microsoft/rStar-Coder](https://huggingface.co/datasets/microsoft/rStar-Coder) (`synthetic_sft`, `seed_sft`) | CC BY 4.0 | 398,183 · 591,660 | Synthetic and human contest seeds |
| [IIGroup/X-Coder-SFT-376k](https://huggingface.co/datasets/IIGroup/X-Coder-SFT-376k) | MIT | 376,491 (verified subset 90,016) | Fully synthetic |
| [nvidia/OpenCodeReasoning](https://huggingface.co/datasets/nvidia/OpenCodeReasoning) | CC BY 4.0 | split_0 567,850 · split_1 167,405 | DeepSeek-R1 distillation |
| [nvidia/OpenCodeReasoning-2](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2) | CC BY 4.0 | Python 120,000 · C++ 100,000 | DeepSeek-R1 distillation |

## Download

```bash
python3 scripts/download.py --list
python3 scripts/download.py agentica-org/DeepCoder-Preview-Dataset
```

`scripts/download.py` calls `huggingface_hub.snapshot_download` and writes under `data/`, which is gitignored. Install `huggingface_hub` first. Row counts and licenses were checked against Hugging Face dataset cards on 2026-09-30.

## License

The catalog, README, and download script in this repository are MIT. Each listed dataset keeps the license on its Hugging Face card. This repository does not grant rights to redistribute those rows.
