import os
import pandas as pd
import psycopg2
from datetime import datetime
import numpy as np
import chardet

# Define your PostgreSQL database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'W@rwick2023!',
    'host': '192.168.128.215',
    'port': '5432',
}

# Define the path to your CSV file
csv_file = r'B:\Code\Ditto\test3.csv'



# Read the CSV file into a df
df = pd.read_csv(csv_file, encoding='iso-8859-1')


df = df.where(pd.notnull(df), None)
df = df.replace(np.nan, None)


# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Iterate through the df and insert data into the PostgreSQL table
    for index, row in df.iterrows():
        insert_query = """
        INSERT INTO liaisons (
            entity_id, entity_name, thread_name, task_id, task_name, "type", "subtype",
            status, assigner, assignee, created_date, modified_date, complete_date,
            ws_team, region, network, primary_referrer, pnm, agreement_type,
            dob, entity_type, id, date_will_logged
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        ON CONFLICT (entity_id, task_id, complete_date) DO NOTHING;
        """
        cursor.execute(insert_query, (
            row['Entity Id'], row['Entity Name'], row['Thread Name'], row['Task ID'],
            row['Task Name'], row['Type'], row['Subtype'], row['Status'], row['Assigner'],
            row['Assignee'], row['Created Date'], row['Modified Date'], row['Complete Date'],
            row['WS Team'], row['Region'], row['Network'], row['Primary Referrer'],
            row['PNM'], row['Agreement Type'], row['Date of Birth'], 
            row['Entity Type'], row['ID'], row['Date Will Logged']
        ))

    conn.commit()

except Exception as e:
    print("Error:", e)

finally:
    # Close the database connection, regardless of whether an error occurred or not
    if 'conn' in locals() and conn is not None:
        cursor.close()
        conn.close()
