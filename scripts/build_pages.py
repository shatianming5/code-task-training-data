#!/usr/bin/env python3
"""Render dataset detail pages and refresh catalog size/file fields.

Sizes are the sum of files on Hugging Face `main` (what snapshot_download
pulls). Hugging Face storage can be larger because of LFS history.
Checked against the Hub tree API on 2026-09-30.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASETS = ROOT / "datasets"

REPOS = [
    {
        "id": "agentica-org/DeepCoder-Preview-Dataset",
        "n_files": 31,
        "size_bytes": 7811998710,
        "hf_storage_bytes": 13603348246,
        "directories": [
            ("lcbv5", 19, 5790246998),
            ("primeintellect", 5, 1159149534),
            ("taco", 4, 862295065),
            ("codeforces", 1, 301694),
        ],
        "files": [
            ("codeforces/test-00000-of-00001.parquet", 301694),
            ("README.md", 2958),
        ],
        "list_all_files": False,
    },
    {
        "id": "NousResearch/RLVR_Coding_Problems",
        "n_files": 4,
        "size_bytes": 9326591999,
        "hf_storage_bytes": 18239939267,
        "directories": [],
        "files": [
            ("rl_train.jsonl", 9326586263),
            ("data_process.py", 3007),
            ("README.md", 217),
        ],
        "list_all_files": True,
    },
    {
        "id": "IIGroup/X-Coder-RL-40k",
        "n_files": 12,
        "size_bytes": 17999573445,
        "hf_storage_bytes": 17999568578,
        "directories": [
            ("syn_rl_data", 5, 9068010669),
            ("real_rl_data", 5, 8931557909),
        ],
        "files": [
            ("real_rl_data/non_sys_prompt/codeforces_9763.parquet", 27904029),
            ("real_rl_data/non_sys_prompt/klear_code.parquet", 2198074877),
            ("real_rl_data/non_sys_prompt/leetcode_2772.parquet", 34107619),
            ("real_rl_data/non_sys_prompt/taco_13064.parquet", 1857617656),
            ("real_rl_data/non_sys_prompt/test_wo_prompt.parquet", 4813853728),
            ("syn_rl_data/xcoder_data/sorted_by_passrate/part_0000.parquet", 65032885),
            ("syn_rl_data/xcoder_data/sorted_by_passrate/part_0001.parquet", 2492359112),
            ("syn_rl_data/xcoder_data/sorted_by_passrate/part_0002.parquet", 1915565359),
            ("syn_rl_data/xcoder_data/sorted_by_passrate/part_0003.parquet", 2452644972),
            ("syn_rl_data/xcoder_data/sorted_by_passrate/part_0004.parquet", 2142408341),
        ],
        "list_all_files": True,
    },
    {
        "id": "Skywork/Skywork-OR1-RL-Data",
        "n_files": 6,
        "size_bytes": 823113220,
        "hf_storage_bytes": 6252922168,
        "directories": [("data", 4, 823104116)],
        "files": [
            ("data/code-00000-of-00003.parquet", 261971378),
            ("data/code-00001-of-00003.parquet", 301173660),
            ("data/code-00002-of-00003.parquet", 240990576),
            ("data/math-00000-of-00001.parquet", 18968502),
            ("README.md", 6539),
        ],
        "list_all_files": True,
    },
    {
        "id": "Kwai-Klear/KlearReasoner-CodeSub-15K",
        "n_files": 3,
        "size_bytes": 4165429235,
        "hf_storage_bytes": 6586796426,
        "directories": [],
        "files": [
            ("train_code_rllm_clean.json", 4165422812),
            ("README.md", 3899),
        ],
        "list_all_files": True,
    },
    {
        "id": "microsoft/rStar-Coder",
        "n_files": 867,
        "size_bytes": 472757580959,
        "hf_storage_bytes": 506050071749,
        "directories": [
            ("synthetic_rl_testcase", 797, 275225780571),
            ("seed_testcase", 30, 178650530799),
            ("seed_sft", 20, 12079419204),
            ("synthetic_sft", 15, 6513436786),
            ("synthetic_rl", 1, 288262511),
        ],
        "files": [],
        "list_all_files": False,
    },
    {
        "id": "open-r1/codeforces",
        "n_files": 2219,
        "size_bytes": 243838668917,
        "hf_storage_bytes": 385043763607,
        "directories": [
            ("verifiable_tests", 469, 118287943707),
            ("generated_tests", 1705, 115397785490),
            ("verifiable-prompts", 20, 4936052469),
            ("data", 12, 2755295134),
            ("verifiable", 11, 2461572745),
        ],
        "files": [],
        "list_all_files": False,
    },
    {
        "id": "likaixin/TACO-verified",
        "n_files": 3,
        "size_bytes": 1925888192,
        "hf_storage_bytes": 2841521015,
        "directories": [],
        "files": [
            ("taco_verified.json", 1925884524),
            ("README.md", 1194),
        ],
        "list_all_files": True,
    },
    {
        "id": "inclusionAI/AReaL-boba-2-RL-Code",
        "n_files": 11,
        "size_bytes": 11229060962,
        "hf_storage_bytes": 28207079485,
        "directories": [
            ("train", 1, 6885257689),
            ("code_benchmark", 7, 4343797761),
        ],
        "files": [
            ("train/train.jsonl", 6885257689),
            ("code_benchmark/codeforces/all_contest_data.json", 1916837001),
            ("code_benchmark/lcb_v5/test.jsonl", 1201484797),
            ("code_benchmark/lcb_v5_2410_2502/test.jsonl", 1201272482),
            ("code_benchmark/code_contest_all/test.jsonl", 23332163),
            ("code_benchmark/codeforces/test.jsonl", 821087),
            ("dataset.py", 1245),
            ("README.md", 1678),
        ],
        "list_all_files": True,
    },
    {
        "id": "IIGroup/X-Coder-SFT-376k",
        "n_files": 123,
        "size_bytes": 23066963099,
        "hf_storage_bytes": 23066955346,
        "directories": [("data", 120, 23066752414)],
        "files": [],
        "list_all_files": False,
    },
    {
        "id": "nvidia/OpenCodeReasoning",
        "n_files": 42,
        "size_bytes": 9731582805,
        "hf_storage_bytes": 13325719641,
        "directories": [
            ("split_0", 30, 8325018575),
            ("split_1", 10, 1406554853),
        ],
        "files": [("README.md", 6868)],
        "list_all_files": False,
    },
    {
        "id": "nvidia/OpenCodeReasoning-2",
        "n_files": 131,
        "size_bytes": 49411866253,
        "hf_storage_bytes": 156753115175,
        "directories": [("train", 129, 49411855237)],
        "files": [("README.md", 11016)],
        "list_all_files": False,
    },
]


def human(n: int) -> str:
    x = float(n)
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if x < 1024 or unit == "TiB":
            return f"{int(x)} B" if unit == "B" else f"{x:.2f} {unit}"
        x /= 1024.0
    raise AssertionError


def slug(dataset_id: str) -> str:
    return dataset_id.replace("/", "--")


def hf_card(dataset_id: str) -> str:
    return f"https://huggingface.co/datasets/{dataset_id}"


def hf_tree(dataset_id: str, path: str = "") -> str:
    base = f"https://huggingface.co/datasets/{dataset_id}/tree/main"
    return f"{base}/{path}" if path else base


def hf_blob(dataset_id: str, path: str) -> str:
    return f"https://huggingface.co/datasets/{dataset_id}/blob/main/{path}"


def hf_viewer(dataset_id: str) -> str:
    return f"https://huggingface.co/datasets/{dataset_id}/viewer"


def page_path(dataset_id: str) -> str:
    return f"datasets/{slug(dataset_id)}.md"


def render_page(repo: dict) -> str:
    did = repo["id"]
    lines = [
        f"# {did}",
        "",
        f"- **Hugging Face card:** [{did}]({hf_card(did)})",
        f"- **Files on Hub:** [{repo['n_files']} files]({hf_tree(did)})",
        f"- **Dataset viewer:** [open viewer]({hf_viewer(did)})",
        f"- **Size on `main`:** {human(repo['size_bytes'])} ({repo['size_bytes']:,} bytes)",
        f"- **Hugging Face storage:** {human(repo['hf_storage_bytes'])} ({repo['hf_storage_bytes']:,} bytes)",
        "",
        "Size on `main` is the sum of current files (what a snapshot download pulls). "
        "Hugging Face storage can be larger because of LFS history.",
        "",
    ]
    if repo["directories"]:
        lines += [
            "## Directories",
            "",
            "| Directory | Files | Size | Link |",
            "| --- | ---: | ---: | --- |",
        ]
        for path, n, nbytes in repo["directories"]:
            lines.append(
                f"| `{path}/` | {n} | {human(nbytes)} | [browse]({hf_tree(did, path)}) |"
            )
        lines.append("")
    files = repo["files"] if repo.get("list_all_files") else repo.get("files") or []
    if repo.get("list_all_files") and files:
        lines += [
            "## Files",
            "",
            "| File | Size | Link |",
            "| --- | ---: | --- |",
        ]
        for path, nbytes in files:
            lines.append(
                f"| `{path}` | {human(nbytes)} | [open]({hf_blob(did, path)}) |"
            )
        lines.append("")
    else:
        lines += [
            f"File list: [{repo['n_files']} files on Hugging Face]({hf_tree(did)}).",
            "",
        ]
    lines += ["Back to the [catalog](../README.md).", ""]
    return "\n".join(lines)


def repo_fields(repo: dict) -> dict:
    return {
        "n_files": repo["n_files"],
        "size_bytes": repo["size_bytes"],
        "size": human(repo["size_bytes"]),
        "hf_storage_bytes": repo["hf_storage_bytes"],
        "hf_storage": human(repo["hf_storage_bytes"]),
        "hf_url": hf_card(repo["id"]),
        "hf_files_url": hf_tree(repo["id"]),
        "hf_viewer_url": hf_viewer(repo["id"]),
        "page": page_path(repo["id"]),
    }


def main() -> None:
    DATASETS.mkdir(exist_ok=True)
    by_id = {r["id"]: r for r in REPOS}
    for old in DATASETS.glob("*.md"):
        old.unlink()
    for repo in REPOS:
        path = ROOT / page_path(repo["id"])
        path.write_text(render_page(repo), encoding="utf-8")

    catalog = json.loads((ROOT / "catalog.json").read_text())
    catalog["hf_checked"] = "2026-09-30"
    catalog["size_note"] = (
        "size is the sum of files on Hugging Face main; "
        "hf_storage is Hub usedStorage and may include LFS history"
    )
    for group in ("rl", "sft"):
        for row in catalog[group]:
            row.update(repo_fields(by_id[row["id"]]))
    (ROOT / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(REPOS)} pages")


if __name__ == "__main__":
    main()
