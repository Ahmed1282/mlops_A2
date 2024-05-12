# Airflow Data Extraction Pipeline

This project automates the data extraction lifecycle by extracting data from specified URLs, transforming it, saving it, versioning the data with DVC, and versioning the code with Git.

## How To Run?

1. Install Apache Airflow in a Python virtual environment:

```bash
pip install apache-airflow
    Set the Airflow environment variable to the root of this cloned repository:

bash

export AIRFLOW_HOME="root of this cloned repo"

    Initialize Airflow database:

bash

airflow db init

    Start the Airflow scheduler in a separate console:

bash

airflow scheduler

    Start the Airflow webserver and open the Airflow user interface at http://localhost:8080:

bash

airflow webserver -p 8080

    Find the DAG with the name specified in the code and toggle the pause button to activate the DAG.

    Click the play button on the top right to manually trigger the DAG run.

DAG Documentation
Extract Task:

Extracts data from a list of URLs (urls) using the extract_data function. Each URL is processed sequentially, and the extracted data is combined.
Preprocess Task:

Preprocesses the extracted data using the clean_data function. This task ensures that the text data is cleaned and formatted consistently.
Save Task:

Saves the preprocessed data to a CSV file specified by filename. The data is saved in the format of 'id', 'title', 'description', and 'source' columns.
DVC Push Task:

Adds the CSV file (data/extracted.csv) to the DVC repository using the dvc add command and pushes the changes to the remote Google Drive storage using dvc push.
Git Push Task:

Performs Git operations to push the changes made to the Git repository. It includes commands to pull changes, add files, commit changes, and push to the remote repository.
DAG Execution Order

The tasks are executed sequentially in the following order:

python

extract_task >> preprocess_task >> save_task >> dvc_push_task >> git_push_task

The DAG is configured to run manually (schedule=None) and does not have a specific schedule for automatic execution.
Encountered Challenges
Challenge: Changing the Airflow configuration to detect DAGs present in locations other than the Airflow folder.

Solution: Make a dags directory in your current folder, place DAGs there, and set the environment variable export AIRFLOW_HOME="current folder".
Challenge: How to automate Git and DVC commands?

Solution: Use the Python os library.
Challenge: Dataset not being saved using Airflow.

Solution: Use absolute paths for the dataset.
Points To Note

    Place all/any DAGs in the /dags folder for Airflow to detect.
    Run airflow dags list to check if Airflow properly picks up DAGs from the DAG bag (DAG folder which contains all DAGs).

vbnet


You can copy this text block and paste it into your README.md file. Let me know if you need further assistance!

