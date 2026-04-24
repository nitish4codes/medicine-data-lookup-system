# Medicine Data Mapping & Lookup System

## Overview
This project is a Python-based data engineering pipeline designed to clean, normalize, and provide highly efficient lookup functionality for large-scale medical datasets (**50,000+ records**). It handles raw, inconsistent CSV data, normalizes string formats, and allows users to query and export structured JSON data based on specific medical parameters.

## Features
* **Large-Scale Data Processing:** Efficiently cleans and normalizes 50,000+ rows of raw medicine records using Pandas.
* **Data Normalization:** Automated lowercasing and whitespace trimming to resolve formatting inconsistencies.
* **Flexible Querying:** Search by medicine name (partial matching) or filter by category and dosage (exact matching).
* **Automated JSON Export:** Generates structured JSON outputs from queried datasets for downstream API consumption.
* **Command-Line Interface (CLI):** Simple and fast terminal-based user interaction.

## Tech Stack
* Python
* Pandas
* CSV (Data ingestion and storage)
* JSON (Data export and integration)

## Project Structure
```text
medicine_project/
│
├── data/
│   └── medicines.csv      # 50,000+ row dataset
├── main.py                # Core ETL and query logic
├── requirements.txt
├── README.md
└── .gitignore
