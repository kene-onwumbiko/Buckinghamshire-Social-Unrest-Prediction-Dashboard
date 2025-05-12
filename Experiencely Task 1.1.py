# -*- coding: utf-8 -*-
"""
Created on Thu May  8 18:14:56 2025

@author: keneo
"""

# Import library
import pandas as pd

# Load the dataset
helpdesk = pd.read_csv(r"C:\Users\keneo\Downloads\helpdesk_tickets.csv")

# Check for missing values
helpdesk_missingvalues = helpdesk.isnull().sum()

# Check for duplicated values
helpdesk_duplicatedvalues = helpdesk.duplicated()

# Check the data types to know if there are inconsistent data
helpdesk_datatypes = helpdesk.dtypes

# Drop unnamed column and columns with no values and save in a new dataframe
new_helpdesk = helpdesk.drop(columns = ["Team Lead", "Unnamed: 22", "SR No.", "Corrective Actions", 
                                        "Preventive Actions", "Closed By"])

# Convert individual columns to datetime format
new_helpdesk['Date Created'] = pd.to_datetime(new_helpdesk['Date Created'], errors='coerce')
new_helpdesk['Last Updated'] = pd.to_datetime(new_helpdesk['Last Updated'], errors='coerce')
new_helpdesk['Due Date'] = pd.to_datetime(new_helpdesk['Due Date'], errors='coerce')

# Drop duplicate rows and keep only unique ones from the new dataframe
new_helpdesk = new_helpdesk.drop_duplicates()

# Drop all rows with any missing values from the new dataframe
new_helpdesk = new_helpdesk.dropna(axis = 0)

# Check for missing values in the new dataframe
new_helpdesk_missingvalues = new_helpdesk.isnull().sum()

# Check for duplicated values in the new dataframe
new_helpdesk_duplicatedvalues = new_helpdesk.duplicated()



