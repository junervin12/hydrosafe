from pathlib import Path

REQUIRED_PATHS = [
    "README.md",
    "DATA_ACCESS.md",
    "REPRODUCIBILITY.md",
    "requirements.txt",
    "config/input_schema.json",
    "config/regulatory_thresholds.json",
    "notebooks/01_hydrosafe_end_to_end_reproducible_workflow.ipynb",
    "outputs/figures",
    "outputs/tables",
    "outputs/reports",
]

root = Path(__file__).resolve().parents[1]
missing = [p for p in REQUIRED_PATHS if not (root / p).exists()]

if missing:
    print("Missing required files or folders:")
    for p in missing:
        print(f"- {p}")
    raise SystemExit(1)

print("Project structure check passed.")
