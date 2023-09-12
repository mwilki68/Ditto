import os
import pandas as pd
import psycopg2
from datetime import datetime
import numpy as np
from configparser import ConfigParser

config_dev = ConfigParser()
# The path below should also be changed when in development 
path = os.path.join('//appsrv', 'business intelligence', 'Code', 'Ditto', 'config_dev.ini')
config_dev.read(path)

# Define your PostgreSQL database connection parameters
db_params = {
    'dbname': config_dev['Conn']['dbname'],
    'user': config_dev['Conn']['user'],
    'password': config_dev['Conn']['password'],
    'host': config_dev['Conn']['host'],
    'port': config_dev['Conn']['port']
}

def insert_liaison(path):\

    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')


    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)

        # Default date value
    default_date = '1753-01-01'
    default_blank = '0'

    df['Task ID'] = df['Task ID'].fillna(default_blank)
    df['Entity Id'] = df['Entity Id'].fillna(default_blank)



    # List of date columns in your DataFrame
    date_columns = ['Complete Date', 'Modified Date', 'Created Date', 'Date of Birth', 'Date Will Logged']

    # Loop through date columns and replace null values with default date
    for col in date_columns:
        df[col] = df[col].fillna(default_date)


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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert_ror(path):\

    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    
    # Default date value
    default_date = '1753-01-01'
    default_blank = '0'

    df['Task ID'] = df['Task ID'].fillna(default_blank)
    df['Entity Id'] = df['Entity Id'].fillna(default_blank)

    # List of date columns in your DataFrame
    date_columns = ['Complete Date', 'Modified Date', 'Created Date', 'Date of Birth', 'Date Will Logged']

    # Loop through date columns and replace null values with default date
    for col in date_columns:
        df[col] = df[col].fillna(default_date)

 
    
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO reviews (
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
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert_wl(path):\

    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    
    # Default date value
    default_date = '1753-01-01'
    default_blank = '0'

    df['Task ID'] = df['Task ID'].fillna(default_blank)
    df['Entity Id'] = df['Entity Id'].fillna(default_blank)

    # List of date columns in your DataFrame
    date_columns = ['Complete Date', 'Modified Date', 'Created Date', 'Date of Birth', 'Date Will Logged']

    # Loop through date columns and replace null values with default date
    for col in date_columns:
        df[col] = df[col].fillna(default_date)

 
    
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO wl (
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
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert_tasks(path):\

    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    
    # Default date value
    default_date = '1753-01-01'
    default_blank = '0'

    df['Task ID'] = df['Task ID'].fillna(default_blank)
    df['Entity Id'] = df['Entity Id'].fillna(default_blank)

    # List of date columns in your DataFrame
    date_columns = ['Complete Date', 'Modified Date', 'Created Date', 'Date of Birth', 'Date Will Logged']

    # Loop through date columns and replace null values with default date
    for col in date_columns:
        df[col] = df[col].fillna(default_date)

 
    
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO tasks (
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
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert_epp(path):\

    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    
    # Default date value
    default_date = '1753-01-01'
    default_blank = '0'

    df['Task ID'] = df['Task ID'].fillna(default_blank)
    df['Entity Id'] = df['Entity Id'].fillna(default_blank)

    # List of date columns in your DataFrame
    date_columns = ['Complete Date', 'Modified Date', 'Created Date', 'Date of Birth', 'Date Will Logged']

    # Loop through date columns and replace null values with default date
    for col in date_columns:
        df[col] = df[col].fillna(default_date)

 
    
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO epp (
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

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_TA(path):

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # delete_all_query = """DELETE FROM teams;"""
    # # Execute the DELETE statement
    # cursor.execute(delete_all_query)

    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    

    # Connect to the PostgreSQL database
    try:

        delete_all_query = """DELETE FROM teams;"""
        # Execute the DELETE statement
        cursor.execute(delete_all_query)


        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO teams (
                entity_id, entity_name, ws, crs, cro, asa, ram, aram, category, network, region, referrer
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
            
            """
            cursor.execute(insert_query, (
                row['Entity ID'], row['Entity Name'], row['Wealth Team'], row['Client Relationship Specialist'],
                row['Client Relationship Officer'], row['Annuity Split Allocation'], row['Key Details | Regional Admin Manager'], 
                    row['Key Details | RAM Assistant'], row['Category'], row['Referral | Network'], row['Region'], row['Primary Referrer']
            ))

        conn.commit()

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the database connection, regardless of whether an error occurred or not
        if 'conn' in locals() and conn is not None:
            cursor.close()
            conn.close()









# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


update_TA(config_dev['Source']['TA'])
insert_liaison(config_dev['Source']['liaisons'])
insert_ror(config_dev['Source']['ror'])
insert_wl(config_dev['Source']['wl'])
insert_tasks(config_dev['Source']['tasks'])
insert_epp(config_dev['Source']['epp'])
