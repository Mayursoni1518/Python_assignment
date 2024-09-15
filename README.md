# Python_assignment
this is assignment Python given by Aadi foundation ( Training classes ) 

# Data Cleaning and Preparation Assignment

## Introduction
This project demonstrates basic data cleaning and preparation techniques using Python and pandas. The dataset used is a sample of customer data, which contains missing values, duplicates, and potential outliers.

## Dataset
The dataset contains the following fields:
- `CustomerID`: Unique ID of the customer.
- `Name`: Name of the customer.
- `Age`: Age of the customer (with missing values).
- `Gender`: Gender of the customer.
- `PurchaseAmount`: Amount spent by the customer (with missing values).
- `City`: City of residence (with missing values).

## Data Cleaning Steps
1. **Remove Duplicate Records**: Duplicates are removed based on the `CustomerID`.
2. **Handle Missing Values**:
   - Missing `Age` values are filled with the average age.
   - Missing `PurchaseAmount` values are filled with the median purchase amount.
   - Missing `City` values are filled with 'Unknown'.
3. **Outlier Detection**: Outliers in the `PurchaseAmount` column were detected using the IQR method, but none were removed in this sample.
4. **Data Type Correction**: The data types of columns were checked, and all were found correct.

## How to Run the Script
1. Install the necessary libraries:
    ```bash
    pip install pandas
    ```
2. Run the Python script or the Jupyter notebook.
3. The cleaned dataset will be printed and saved as a CSV file (`cleaned_data.csv`).

## Files in the Repository
- `data_cleaning.py`: Python script containing the data cleaning code.
- `cleaned_data.csv`: The cleaned version of the dataset.
- `README.md`: Explanation of the assignment.
