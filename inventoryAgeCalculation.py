"""
Module Name: Inventory Age Calculation
Description: This module calculates the age of inventory items based on event dates and types.
Author: Abhishek Shah
Date: 05/23/2023
"""

# Import required modules
from collections import defaultdict
from datetime import datetime

# Sample data from Table 1
table1 = [
    {"ID": "TR0013", "OnHandQuantity": 278, "OnHandQuantityDelta": 99, "event_type": "OutBound", "event_datetime": "25/05/2020 00:25"},
    {"ID": "TR0012", "OnHandQuantity": 377, "OnHandQuantityDelta": 31, "event_type": "InBound", "event_datetime": "24/05/2020 22:00"},
    # Add more entries from Table 1...
]

# Initialize count variables
count_0_90_days = 0
count_91_180_days = 0
count_181_270_days = 0
count_271_365_days = 0

# Convert event_datetime to datetime object and calculate age in days
today = datetime.now()
for entry in table1:
    event_date = datetime.strptime(entry["event_datetime"], "%d/%m/%Y %H:%M")
    age = (today - event_date).days

    # Categorize the entry based on its age and event type
    if age <= 90:
        if entry["event_type"] == "InBound":
            count_0_90_days += entry["OnHandQuantityDelta"]
        elif entry["event_type"] == "OutBound":
            count_0_90_days -= entry["OnHandQuantityDelta"]
    elif 91 <= age <= 180:
        if entry["event_type"] == "InBound":
            count_91_180_days += entry["OnHandQuantityDelta"]
        elif entry["event_type"] == "OutBound":
            count_91_180_days -= entry["OnHandQuantityDelta"]
    elif 181 <= age <= 270:
        if entry["event_type"] == "InBound":
            count_181_270_days += entry["OnHandQuantityDelta"]
        elif entry["event_type"] == "OutBound":
            count_181_270_days -= entry["OnHandQuantityDelta"]
    elif 271 <= age <= 365:
        if entry["event_type"] == "InBound":
            count_271_365_days += entry["OnHandQuantityDelta"]
        elif entry["event_type"] == "OutBound":
            count_271_365_days -= entry["OnHandQuantityDelta"]

# Create Table 2 to store the summarized inventory counts
table2 = {
    "0-90 days old": count_0_90_days,
    "91-180 days old": count_91_180_days,
    "181-270 days old": count_181_270_days,
    "271-365 days old": count_271_365_days
}

# Print Table 2
print("Table 2")
print("--------------")
for age_range, count in table2.items():
    print(f"{age_range}: {count}")
