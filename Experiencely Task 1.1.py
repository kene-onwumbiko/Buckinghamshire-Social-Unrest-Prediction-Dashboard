# -*- coding: utf-8 -*-
"""
Created on Thu May  8 18:14:56 2025

@author: keneo
"""

import pandas as pd

# Load the dataset
helpdesk = pd.read_csv(r"C:\Users\keneo\Downloads\helpdesk_tickets.csv")

# Check for missing values
helpdesk_missingvalues = helpdesk.isnull().sum()

# Check for duplicated values
helpdesk_duplicatedvalues = helpdesk.duplicated()

# Check the data types
helpdesk_datatypes = helpdesk.dtypes

# Drop unnamed column and columns with no values
new_helpdesk = helpdesk.drop(columns = ["Team Lead", "Unnamed: 22", "SR No.", "Corrective Actions", 
                                        "Preventive Actions", "Closed By"])

# Drop duplicate rows and keep only unique ones
new_helpdesk = new_helpdesk.drop_duplicates()

# # Drop all columns with missing values
# new_helpdesk = helpdesk.dropna(axis=1)

# # Check for missing values
# new_helpdesk_missingvalues = new_helpdesk.isnull().sum()

# # Check for duplicated values
# new_helpdesk_duplicatedvalues = new_helpdesk.duplicated()



