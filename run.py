import pandas as pd
from datetime import date, datetime, timedelta
import os
import csv


today = date.today()


# Define the expected headers for each CSV type
car_headers = ["id", "vin", "make", "model", "year"]
maintenance_headers = ["id", "vin", "type", "in-shop date", "out of shop date", "cost", "vendor"]
geo_headers = ["trip id", "vin", "mileage start", "mileage end", "engine status", "trip type"]

# Function to check the headers
def check_csv_headers(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        
        # Compare the headers with the predefined headers
        if headers == car_headers:
            return "Car Data"
        elif headers == maintenance_headers:
            return "Maintenance Data"
        elif headers == geo_headers:
            return "Geo Data"
        else:
            return "Unknown Data Type"

# Example usage
file_path = 'your_file.csv'
result = check_csv_headers(file_path)
print(f'The CSV file contains: {result}')