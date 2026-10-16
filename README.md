# Data Ingestion Project

A Python-based project for reading and exploring CSV datasets, built as part of my journey into **Data Engineering**.

This project starts with loading raw CSV files and inspecting their structure. It will serve as a foundation for developing a more complete data pipeline that includes data validation, cleaning, transformation, and loading.

## Project Objectives

- Practice reading and processing CSV files using Python.
- Explore datasets and understand their structure before processing.
- Learn the fundamentals of data ingestion and pipeline development.
- Gradually build a reusable data pipeline following data engineering practices.

## Current Features

- **CSV file discovery** — Finds CSV files inside the `data/` directory.
- **Interactive file selection** — Allows the user to select a dataset from the available files.
- **Data loading** — Reads the selected CSV file into a pandas DataFrame.
- **Data preview** — Displays the first five rows of the dataset.
- **Dataset dimensions** — Shows the number of rows and columns.
- **Column inspection** — Lists the dataset's column names.
- **Data type inspection** — Displays the data type of each column.
- **Descriptive statistics** — Generates summary statistics for supported data columns.
- **Basic input handling** — Handles invalid numeric input and missing CSV files.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| pandas | Loading and inspecting tabular data |
| glob | Discovering CSV files in the data directory |
| Git and GitHub | Version control and project tracking |

## Project Structure

```text
data-ingestion-project/
├── data/
│   └── sample.csv
├── main.py
├── README.md
└── .gitattributes
```

The CSV file shown above is an example of the expected data location. Your actual dataset filenames may differ.

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/victornagum/data-ingestion-project.git
cd data-ingestion-project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install the dependency

```bash
pip install pandas
```

### 4. Add a CSV dataset

Place one or more CSV files inside the `data/` directory.

For example:

```text
data/
├── employees.csv
└── transactions.csv
```

Use datasets that you have permission to access and that do not expose confidential information.

### 5. Run the project

```bash
python main.py
```

Select one of the listed CSV files when prompted. The program will display a preview of the selected dataset, its dimensions, column names, data types, and descriptive statistics.

## How It Works

The current workflow follows these steps:

1. Discover CSV files in the `data/` directory.
2. Display the available files.
3. Accept the user's file selection.
4. Load the selected dataset using pandas.
5. Inspect the dataset's contents and structure.
6. Display basic descriptive statistics.

```text
CSV Files
    |
    v
File Discovery
    |
    v
User Selects a File
    |
    v
Load with pandas
    |
    v
Inspect Dataset
    |
    v
Display Summary
```

## Roadmap

The following are planned improvements, not features currently implemented.

- [ ] Validate required columns and data types.
- [ ] Detect missing values and duplicate records.
- [ ] Identify and handle invalid data.
- [ ] Clean and standardize datasets.
- [ ] Separate ingestion, validation, and transformation logic into reusable functions.
- [ ] Add structured logging and error handling.
- [ ] Load processed data into a target database.
- [ ] Add automated tests.
- [ ] Explore pipeline automation and scheduling.

## Learning Outcomes

Through this project, I am developing practical skills in:

- Python programming and data manipulation.
- CSV ingestion and dataset inspection.
- Understanding data quality and validation.
- Breaking data processing tasks into manageable steps.
- Version control using Git and GitHub.
- Building a foundation for ETL/ELT pipelines.

## Project Status

**In Progress**

This is a learning and portfolio project. Its scope will expand as I implement additional data engineering concepts and improve the pipeline's reliability and maintainability.

## Author

**Victor Nagum**

GitHub: [@victornagum](https://github.com/victornagum)

---

*This project is part of my ongoing journey to develop practical Data Engineering skills through hands-on implementation.*
