# Reproducibility Guide

This document describes how to reproduce the HydroSafe scientific analysis workflow for manuscript-ready tables, figures, and summary reports.

## 1. Environment setup

Create a clean Python environment and install the required packages:

```bash
pip install -r requirements.txt
```

Alternatively, create a Conda environment:

```bash
conda env create -f environment.yml
conda activate hydrosafe
```

## 2. Dataset preparation

Place the source dataset in:

```text
data/raw/heavy_metal_dataset_with_target.csv
```

If redistribution of the raw dataset is not permitted, download the public dataset from Kaggle following the instructions in `DATA_ACCESS.md` and place it in the same path.

## 3. Running the main notebook

Run the notebook below from the first cell to the last cell:

```text
notebooks/01_hydrosafe_end_to_end_reproducible_workflow.ipynb
```

The notebook performs:

1. package import and runtime configuration;
2. dataset loading and validation;
3. preprocessing and feature engineering;
4. regulatory threshold mapping;
5. exploratory data analysis;
6. repeated cross-validation;
7. final model training and test evaluation;
8. deep learning experiments;
9. digital twin status mapping;
10. interpretability analysis;
11. sensitivity and uncertainty simulation;
12. export of tables, figures, reports, and metadata.

## 4. Expected outputs

After successful execution, the workflow exports:

- manuscript-ready tables in `outputs/tables/`,
- manuscript-ready figures in `outputs/figures/`,
- summary reports in `outputs/reports/`,
- reproducibility metadata and configuration files,
- optional model artifacts in `outputs/models/`.

## 5. Verification

Run the project structure check:

```bash
python scripts/check_project_structure.py
```

Regenerate the file checksum manifest:

```bash
python scripts/create_file_manifest.py
```

The generated checksums can be compared with `FILE_MANIFEST_SHA256.tsv` to verify file integrity.