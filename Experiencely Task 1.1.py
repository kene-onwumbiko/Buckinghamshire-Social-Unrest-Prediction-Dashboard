# -*- coding: utf-8 -*-
"""
Created on Thu May  8 18:14:56 2025

@author: keneo
"""

# Import library
import numpy as np
import pandas as pd

# Load the dataset
helpdesk = pd.read_csv(r"C:\Users\keneo\Downloads\helpdesk_tickets.csv")




# CHECK FOR MISSING VALUES, DUPLICATED VALUES, AND INCONSISTENT DATA
# Check for missing values
helpdesk_missingvalues = helpdesk.isnull().sum()

# Check for duplicated values
helpdesk_duplicatedvalues = helpdesk.duplicated()

# Check the data types for inconsistent data
helpdesk_datatypes = helpdesk.dtypes




# HANDLE DATA CORRECTION
# Drop unnamed column and columns with no values and save in a new dataframe
new_helpdesk = helpdesk.drop(columns = ["Team Lead", "Unnamed: 22", "SR No.", "Corrective Actions", 
                                        "Preventive Actions", "Closed By"])

# Convert columns with date and time to the correct datetime format
for col in ["Date Created", "Last Updated", "Due Date"]:
    if col in new_helpdesk.columns:
        new_helpdesk[col] = pd.to_datetime(new_helpdesk[col])

# Fill missing date in "Due Date" with a random value between 1 to 31 days before the date in "Last Updated"

# This is based on the observation that most of the dates in the "Due Date" column occur a few days before 
# the corresponding dates in the "Last Updated" column.
new_helpdesk["Due Date"] = new_helpdesk.apply(
    lambda row: row["Last Updated"] - pd.Timedelta(days = np.random.randint(1, 32))
    if pd.isna(row["Due Date"]) and pd.notna(row["Last Updated"]) else row["Due Date"],
    axis = 1
)

# Fill missing values in the "Type" column with "Incident / Problem"

# The two rows with missing values in the "Type" column have "Subject" entries that are similar to 
# those in rows where the "Type" is "Incident / Problem." This suggests that "Incident / Problem" is 
# the most appropriate value to fill in for those missing entries. 
new_helpdesk["Type"] = new_helpdesk["Type"].fillna("Incident / Problem")

# Fill missing values in "Category", "Issue Origin", and "Select Ticket Status Update" with a random pick from its unique values

# This is because the values in "Category", "Issue Origin", and "Select Ticket Status Update" columns are 
# highly varied, making it difficult to identify any reliable pattern for filling in the missing data. 
for column in ["Category", "Issue Origin", "Select Ticket Status Update"]:
    unique_values = new_helpdesk[column].dropna().unique()
    new_helpdesk[column] = new_helpdesk[column].apply(
        lambda x: np.random.choice(unique_values) if pd.isna(x) else x
    )

# Drop duplicate rows and keep only unique ones from the new dataframe
new_helpdesk = new_helpdesk.drop_duplicates()




# CHECK FOR MISSING VALUES, DUPLICATED VALUES, AND INCONSISTENT DATA IN THE NEW DATAFRAME
# Check for missing values
new_helpdesk_missingvalues = new_helpdesk.isnull().sum()

# Check for duplicated values
new_helpdesk_duplicatedvalues = new_helpdesk.duplicated()

# Check the data types for inconsistent data
new_helpdesk_datatypes = new_helpdesk.dtypes




# Save the new dataframe to a CSV file
new_helpdesk.to_csv("new_helpdesk_tickets.csv", index = False)