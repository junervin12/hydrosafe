# HydroSafe: Data and Code Availability Package

This repository contains the reproducible research workflow, manuscript-ready tables, figures, documentation, and cleaned code supporting the study:

**A Digital Twin Framework for Deep Learning-Based Heavy Metal Water Contamination Detection Using Carbon Nanomaterial Sensor Response Modeling**

HydroSafe is a data-driven digital twin framework for heavy metal water contamination monitoring using electrochemical carbon-nanomaterial sensor-response data. The workflow combines data cleaning, physics-inspired feature engineering, regulatory threshold mapping, machine learning baselines, deep learning models, interpretability analysis, sensitivity simulation, uncertainty analysis, and manuscript-ready reporting.

---

## Repository structure

```text
HydroSafe_Data_Code_Availability/
├── README.md
├── DATA_ACCESS.md
├── REPRODUCIBILITY.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── environment.yml
├── FILE_MANIFEST_SHA256.tsv
├── config/
│   ├── input_schema.json
│   ├── regulatory_thresholds.json
│   ├── sample_payload.json
│   └── config_template.yaml
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── data_dictionary.md
│   ├── figure_list.md
│   └── table_list.md
├── notebooks/
│   ├── 01_hydrosafe_end_to_end_reproducible_workflow.ipynb
│   └── README.md
├── scripts/
│   ├── check_project_structure.py
│   └── create_file_manifest.py
└── outputs/
    ├── figures/
    ├── tables/
    ├── reports/
    └── models/
```

---

## Main workflow

The main reproducible notebook is:

```text
notebooks/01_hydrosafe_end_to_end_reproducible_workflow.ipynb
```

It performs the complete scientific workflow:

1. environment and dependency setup;
2. dataset loading and integrity checking;
3. data cleaning and missing-value assessment;
4. regulatory threshold mapping using WHO-based metal-specific thresholds;
5. feature engineering for electrochemical impedance and water-quality variables;
6. exploratory data analysis;
7. repeated cross-validation for model robustness assessment;
8. final machine learning model training and test evaluation;
9. deep learning model training using MLP and 1D-CNN architectures;
10. concentration-driven digital twin decision mapping;
11. model interpretability using feature importance and SHAP-compatible summaries;
12. pH sensitivity simulation;
13. Monte Carlo uncertainty simulation;
14. export of manuscript-ready tables, figures, schemas, and summary reports.

---

## Scientific task definition

HydroSafe addresses three linked prediction and decision tasks:

| Task | Output | Role in the framework |
|---|---|---|
| Heavy metal identification | Cd, Pb, Hg, or Cu | Estimates the contaminant type from electrochemical sensor-response features |
| Concentration estimation | Concentration in mg/L | Main numerical output for sensor-response modeling |
| Regulatory digital twin mapping | Safe, Low contamination, Moderate contamination, Heavy contamination | Converts predicted concentration into interpretable water-contamination status using metal-specific thresholds |

The primary decision pipeline is:

```text
Electrochemical sensor-response features
        ↓
Predicted heavy metal type
        ↓
Predicted concentration
        ↓
Metal-specific regulatory threshold
        ↓
Exceedance ratio
        ↓
Contamination status and safety status
```

---

## Dataset

The source dataset is the public Kaggle dataset:

**Electrochemical Heavy Metal Sensor Data**

The dataset contains electrochemical sensor-response features for heavy metal detection. The package includes either the dataset copy used in the analysis or a documented path for obtaining it, depending on redistribution constraints. If the journal or dataset license restricts redistribution, remove the raw dataset from `data/raw/` and retain only the download instructions in `DATA_ACCESS.md`.

---

## Feature groups

| Feature group | Examples |
|---|---|
| Frequency and impedance | Frequency, real impedance, imaginary impedance, magnitude, phase |
| Sensor equivalent-circuit proxy | Charge transfer resistance, double layer capacitance |
| Water-quality condition | Temperature, pH, conductivity |
| Engineered sensor-response features | impedance ratio, magnitude log transform, conductance proxy, phase sine/cosine, Rct-Cdl product |
| Regulatory targets | threshold, exceedance ratio, contamination status, safety status |

---

## Main manuscript-ready outputs

| Path | Description |
|---|---|
| `outputs/tables/` | CSV and Excel tables for manuscript reporting |
| `outputs/tables/all_paper_tables_consolidated.xlsx` | Consolidated workbook of the main result tables |
| `outputs/figures/` | Manuscript-ready figures generated from the workflow |
| `outputs/reports/manuscript_results_summary.md` | Compact results summary for manuscript writing |
| `config/input_schema.json` | Input feature schema used by the modeling workflow |
| `config/regulatory_thresholds.json` | WHO/EPA threshold metadata used in the digital twin mapping |

---

## Key reported results

The main results should be verified from the generated tables and the summary report in `outputs/reports/`. In the completed run used for manuscript drafting, the strongest concentration regressor achieved high predictive performance, and the regulatory digital twin pipeline produced interpretable contamination-status and safety-status predictions based on concentration-to-threshold mapping.

---

## Reproducibility instructions

Create a clean Python environment and install dependencies:

```bash
pip install -r requirements.txt
```

Then run the notebook:

```text
notebooks/01_hydrosafe_end_to_end_reproducible_workflow.ipynb
```

For Google Colab, enable GPU acceleration if deep learning experiments are required:

```text
Runtime → Change runtime type → GPU
```

The notebook automatically exports figures, tables, processed data, metadata, and summary reports to the configured output directory.

---

## Data and code availability statement

The source dataset used in this study is publicly available from Kaggle under the dataset title *Electrochemical Heavy Metal Sensor Data*. This repository provides reproducibility notebooks, feature-engineered data, manuscript-ready tables, figures, and documentation. 
---

## Citation

If this repository supports a publication, cite the manuscript and use the metadata in `CITATION.cff`.

---

## License

Code is released under the MIT License unless otherwise specified. Data redistribution must follow the terms of the original Kaggle dataset and any third-party sources.
