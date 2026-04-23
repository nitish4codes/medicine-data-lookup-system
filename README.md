# Medicine Data Mapping & Lookup System

## Overview

This project is a Python-based data processing system designed to handle inconsistent medicine data and provide efficient lookup functionality.

It normalizes raw medicine records and allows users to query data based on different parameters.

---

## Features

* Data cleaning and normalization (lowercasing and trimming)
* Search by medicine name (partial matching)
* Filter by category and dosage (exact matching)
* JSON export of query results
* Simple command-line interface

---

## Tech Stack

* Python
* Pandas
* CSV (data storage)
* JSON (data export)

---

## Project Structure

medicine_project/
│
├── data/
│   └── medicines.csv
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

---

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the program:
   python main.py

---

## Example Usage

* Search by name:
  Input: pcm
  Output: Returns medicines containing "pcm"

* Filter by category:
  Input: analgesic
  Output: Returns all analgesic medicines

* Filter by dosage:
  Input: 500mg
  Output: Returns medicines with 500mg dosage

---

## Key Concepts Used

* Data preprocessing and normalization
* Data filtering using Pandas
* Handling user input
* JSON data formatting and export

---

## Future Improvements

* Add fuzzy matching for better search accuracy
* Convert into a REST API using Flask
* Integrate with a database (MySQL / MongoDB)
* Add a web-based UI

---

## Author

Nitish Bhardwaj
