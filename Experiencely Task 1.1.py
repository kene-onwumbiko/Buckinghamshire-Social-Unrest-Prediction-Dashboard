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

# Check for missing values
helpdesk_missingvalues = helpdesk.isnull().sum()

# Check for duplicated values
helpdesk_duplicatedvalues = helpdesk.duplicated()

# Check the data types for inconsistent data
helpdesk_datatypes = helpdesk.dtypes

# Drop unnamed column and columns with no values and save in a new dataframe
new_helpdesk = helpdesk.drop(columns = ["Team Lead", "Unnamed: 22", "SR No.", "Corrective Actions", 
                                        "Preventive Actions", "Closed By"])

# # Convert the columns with date and time to datetime format
# new_helpdesk["Date Created"] = pd.to_datetime(new_helpdesk["Date Created"])
# new_helpdesk["Last Updated"] = pd.to_datetime(new_helpdesk["Last Updated"])
# new_helpdesk["Due Date"] = pd.to_datetime(new_helpdesk["Due Date"])

# Convert columns with date and time to the correct datetime format
datetime_columns = ["Date Created", "Last Updated", "Due Date"]

for col in datetime_columns:
    if col in new_helpdesk.columns:
        new_helpdesk[col] = pd.to_datetime(new_helpdesk[col])

# Fill missing date in "Due Date" with a random value between 1 to 31 days before the date in "Last Updated"
new_helpdesk["Due Date"] = new_helpdesk.apply(
    lambda row: row["Last Updated"] - pd.Timedelta(days = np.random.randint(1, 32))
    if pd.isna(row["Due Date"]) and pd.notna(row["Last Updated"]) else row["Due Date"],
    axis = 1
)

# Drop duplicate rows and keep only unique ones from the new dataframe
new_helpdesk = new_helpdesk.drop_duplicates()

# # Drop all rows with any missing values from the new dataframe
# new_helpdesk = new_helpdesk.dropna(axis = 0)

# # Fill all missing values with 'N/A'
# new_helpdesk.fillna("N/A", inplace = True)

# Check for missing values in the new dataframe
new_helpdesk_missingvalues = new_helpdesk.isnull().sum()

# Check for duplicated values in the new dataframe
new_helpdesk_duplicatedvalues = new_helpdesk.duplicated()



