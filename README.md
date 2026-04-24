# Medicine Data Mapping & Lookup System

## Overview
This project is a Python-based data engineering pipeline designed to clean, normalize, and provide highly efficient lookup functionality for large-scale medical datasets (**50,000+ records**). It handles raw, inconsistent CSV data, normalizes string formats, and allows users to query and export structured JSON data based on specific medical parameters.

## Features
* **Large-Scale Data Processing:** Efficiently cleans and normalizes 50,000+ rows of raw medicine records using Pandas.
* **Data Normalization:** Automated lowercasing and whitespace trimming to resolve formatting inconsistencies.
* **Flexible Querying:** Search by medicine name (partial matching) or filter by category and dosage (exact matching).
* **Automated JSON Export:** Generates structured JSON outputs from queried datasets for downstream consumption and data integration.
* **Command-Line Interface (CLI):** Simple and fast terminal-based user interaction for real-time data retrieval.

## Tech Stack
* **Python**
* **Pandas**
* **CSV** (Data ingestion and storage)
* **JSON** (Data export and integration)

## Project Structure
```text
medicine_project/
│
├── data/
│   └── medicines.csv      # Large-scale dataset (50,000+ rows)
├── main.py                # Core ETL and search logic
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore configuration
```
## How to Run
* **Install dependencies:**


  pip install -r requirements.txt
* **Run the program:**


  python main.py
## Example Usage
* **Search by name:**
 
  Input: pcm

  Output: Returns all records containing "pcm" (e.g., PCM 500 mg, Paracetamol 500mg).

* **Filter by category:**

  Input: analgesic

  Output: Returns all records categorized as "Analgesic".

* **Filter by dosage:**

  Input: 500mg

  Output: Returns records matching the "500mg" dosage strength.

## Future Improvements
Fuzzy Matching: Implement Levenshtein distance for improved search accuracy against user typos.

REST API: Transition the project into a web service using Flask or FastAPI.

Database Integration: Move from CSV storage to a structured database like SQLite or PostgreSQL for improved scalability.

## Author
Nitish Bhardwaj


