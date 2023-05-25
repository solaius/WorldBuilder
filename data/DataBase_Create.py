import pandas as pd
import openpyxl
import sqlite3
import re

# Connect to the SQLite database
conn = sqlite3.connect('world_builder.db')

# Read the Excel file using pandas
excel_file = pd.ExcelFile('World Builder Properties.xlsx')
sheet_names = excel_file.sheet_names[1:]

# Iterate over each sheet in the Excel file
for sheet_name in sheet_names:
    # Read the sheet as a DataFrame
    df = excel_file.parse(sheet_name)

    # Clean the sheet name for table name
    cleaned_sheet_name = re.sub(r'\s+', '_', sheet_name)

    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Clean the column name for table name
        cleaned_column_name = re.sub(r'\s+', '_', column.strip())

        # Get the table name as the combination of sheet name and column header
        table_name = cleaned_sheet_name + '_' + column

        # Get the column data as string values
        column_data = df[column].astype(str)

        # Create a new table with the table name and insert the column data into SQLite
        column_data.to_sql(table_name, conn, if_exists='replace', index=False, dtype='TEXT')

# Close the connection
conn.close()
