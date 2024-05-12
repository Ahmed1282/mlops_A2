# MLOps Assignment II: Apache Airflow Implementation

## Overview

This repository contains the solution for Assignment II of the MLOps course, focusing on the implementation of Apache Airflow to automate data extraction, transformation, and version-controlled storage.

## Assignment Details

The objective of this assignment is to implement Apache Airflow to automate the following tasks:

1. **Data Extraction:**
   - Utilize `dawn.com` and `BBC.com` as data sources.
   - Extract links from the landing pages.
   - Extract titles and descriptions from articles displayed on the homepages.

2. **Data Transformation:**
   - Preprocess the extracted text data, ensuring it is cleaned and formatted appropriately for further analysis.

3. **Data Storage and Version Control:**
   - Store the processed data on Google Drive.
   - Implement Data Version Control (DVC) to track versions of the data, ensuring accurate recording of changes.
   - Version metadata against each DVC push to the GitHub repository.

4. **Apache Airflow DAG Development:**
   - Write an Airflow DAG to automate the processes of extraction, transformation, and storage.
   - Ensure effective handling of task dependencies and error management within the DAG.

## Solution Structure

- **`airflow_dags/`:** Contains the Airflow DAG script (`mlops_assignment_ii.py`) responsible for automating the tasks.
- **`data_preprocessing/`:** Documentation of the data preprocessing steps.
- **`dvc_setup/`:** Documentation of the DVC setup, including instructions on versioning metadata against each push to the GitHub repository.

## Usage

1. **Clone the Repository:**
   **git clone https://github.com/Ahmed1282/mlops_A2.git**

2. **Setup Apache Airflow:**
- Install Apache Airflow as per the official documentation: [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- Configure Airflow to recognize the `airflow_dags/` directory.

3. **Run the Airflow DAG:**
- Start the Airflow scheduler and webserver.
- Navigate to the Airflow UI and trigger the DAG `mlops_assignment_ii`.

4. **Review Documentation:**
- Refer to the `data_preprocessing/` and `dvc_setup/` directories for detailed documentation on data preprocessing and DVC setup.

## Contributors

- [Ahmed Baig](https://github.com/Ahmed1282)

