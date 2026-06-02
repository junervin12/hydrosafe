# Data Dictionary

This document describes the main variables used in the HydroSafe reproducible workflow.

## Feature columns

| Column | Description |
|---|---|
| `Frequency_Hz` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Real_Impedance_ohm` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Imag_Impedance_ohm` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Magnitude_ohm` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Phase_deg` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Charge_Transfer_Resistance_ohm` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Double_Layer_Capacitance_F` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Temperature_C` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `pH` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Conductivity_uS_cm` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Real_Impedance_abs` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Imag_Impedance_abs` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Impedance_real_imag_ratio` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Impedance_magnitude_log1p` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Frequency_log10` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Charge_Transfer_Resistance_log1p` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Capacitance_log10_abs` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Conductance_proxy` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Phase_rad` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Phase_sin` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Phase_cos` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Temp_pH_interaction` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Conductivity_pH_ratio` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Rct_Cdl_product` | Sensor-response or engineered predictor used by the machine-learning pipeline |
| `Normalized_Rct_by_Z` | Sensor-response or engineered predictor used by the machine-learning pipeline |

## Target columns

| Column | Description |
|---|---|
| `Metal_Type` | Heavy metal class label in the dataset. |
| `Concentration_mg_L` | Heavy metal concentration in mg/L. |
| `regulatory_threshold_mg_L` | Metal-specific threshold used for the selected regulatory standard. |
| `exceedance_ratio` | Concentration divided by the selected metal-specific threshold. |
| `Contamination_Status_Regulatory` | Regulatory contamination class derived from exceedance ratio. |
| `Safety_Status_Regulatory` | Binary safety label derived from exceedance ratio. |

## Regulatory thresholds

| Standard | Metal | Threshold (mg/L) | Basis | Type |
|---|---:|---:|---|---|
| WHO_2022 | Cd | 0.003 | WHO guideline value for cadmium in drinking water | guideline |
| WHO_2022 | Pb | 0.01 | WHO provisional guideline value for lead in drinking water | provisional guideline |
| WHO_2022 | Hg | 0.006 | WHO guideline value for inorganic mercury in drinking water | guideline |
| WHO_2022 | Cu | 2.0 | WHO health-based/aesthetic guideline value for copper in drinking water | guideline |
| EPA_NPDWR | Cd | 0.005 | EPA MCL for cadmium | MCL |
| EPA_NPDWR | Pb | 0.01 | EPA lead action/trigger-level framing; older action level often reported as 0.015 mg/L | action/trigger level |
| EPA_NPDWR | Hg | 0.002 | EPA MCL for inorganic mercury | MCL |
| EPA_NPDWR | Cu | 1.3 | EPA copper action level | action level |

## Regulatory status rule

```text
Safe if concentration / threshold <= 1
Low contamination if <= 5
Moderate contamination if <= 20
Heavy contamination if > 20
```
