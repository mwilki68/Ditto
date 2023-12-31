import os
import pandas as pd
import psycopg2
from datetime import datetime
import numpy as np
from configparser import ConfigParser
import time 


start_time = time.time()

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

def update_referrers(path):

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()


    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    


    # Connect to the PostgreSQL database
    try:

        delete_all_query = """DELETE FROM referrers;"""
        # Execute the DELETE statement
        cursor.execute(delete_all_query)


        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO referrers (
                entity_id, network, referrer_code, referrer_name, referrer_company_name, 
                first_name, last_name, preferred_name, salultation, club_president, club_contact_person, 
                preferred_email, preferred_phone, street, suburb, province, postcode, referrer_category, 
                region, ws, xplan_linked_profile_entity_id, kicker_deal_applicable, kicker_deal_broker, upfronts_earned, 
                kicker_deal_earned, max_invest_clients, sponsorship_level, date_created, agreement_type, 
                merger_start_date, merger_end_date, merger_fum, pnm, club_category, "subscription"
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            
            """
            cursor.execute(insert_query,(
                row['Referrer Entity ID'], row['Network'], row['Referrer Code'], row['Referrer Xplan Name'], row['Referrer Company Name'], row['First Name'], row['Surname'], row['Preferred Name'], row['Salutation/Greeting'], row['Club President'], row['Club Contact Person'], row['Preferred Email'], row['Preferred Phone'], row['Street'], row['Suburb'], 
                row['State/Province'], row['Postcode'], row['Referrer Category'], row['Region'], row['Wealth Team'], row['Xplan Linked Profile Entity ID'], row['Kicker Deal Applicable'], row['Kicker Deal Broker'], row['Upfronts Earned'], row['Kicker Deal Earned'], row['Max Invest Clients'], row['Sponsorship Level'], row['Date Created'], row['Agreement Type'], row['Merger Start Date'], row['Merger End Date'], 
                row['Merger FUM'], row['PNM'], row['Club Category'], row['Subscription']
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

def update_staff(path):

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()


    # Read the CSV file into a df
    df = pd.read_excel(path)

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    
    # Connect to the PostgreSQL database
    try:

        delete_all_query = """DELETE FROM staff;"""
        # Execute the DELETE statement
        cursor.execute(delete_all_query)


        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO staff ("order", xplan_name, first_name, last_name, user_status, dashboard_status, regional_office, sales_team_category, 
            job_title_short, category, advisory, job_title_long, team_name, 
            sort_order, region, area, hex, font)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query,(
                row['Order'], row['Xplan Name'], row['First Name'], row['Surname'], row['User Status'], row['Dashboards Status'], row['Regional Office'], row['Sales Team Category (Description)'], 
                row['Job Title Short (Adviser Code)'], row['Category'], row['Advisory'], row['Job Title Long'], row['Team Name'], row['Sort Order'], row['Region'], 
                row['Area'], row['HEX'], row['Font (HEX)'] 
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
def update_contact(path):

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()


    # Specify data types for specific columns
    dtype_options = {
        'Entity Id': int,
        'Area Code': str,
        'Country Code': str,
        'Detail': str,
        'Extension': str,
        'Integration Indicator': str,
        'List Item Index': str,
        'List Item Last Modified': str,
        'List Item Last Modified By': str,
        'Name': str,
        'Notes': str,
        'Position': str,
        'Preferred': str,
        'Preferred SMS Mobile': str,
        'Source': str,
        'Source Entity': str,
        'Source Index': str,
        'Type': str,
        'Unknown': str,
        'Update From Datafeed': str
    }

    # Read the CSV file with dtype options
    df = pd.read_csv(path, encoding='iso-8859-1', dtype=dtype_options)

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    

        # Default date value
    default_date = '1753-01-01'
    default_blank = '0'

    df['Entity Id'] = df['Entity Id'].fillna(default_blank)
    df['List Item Index'] = df['List Item Index'].fillna(default_blank)
    df['Type'] = df['Type'].fillna(default_blank)


    # List of date columns in your DataFrame
    date_columns = ['List Item Last Modified']
    # Loop through date columns and replace null values with default date
    for col in date_columns:
        df[col] = df[col].fillna(default_date)


    # Connect to the PostgreSQL database
    try:

        delete_all_query = """DELETE FROM contact;"""
        # Execute the DELETE statement
        cursor.execute(delete_all_query)


        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO contact (entity_id, "area_code", country_code, detail, "extension", integration_indicator, list_item_index, list_item_last_modified, 
            list_item_last_modified_by, "name", notes, "position", preferred, preferred_sms_mobile, "source", 
            source_entity, source_index, "type", unkown, update_from_datafeed)
            VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)
            """
            cursor.execute(insert_query,(
                row['Entity Id'],row['Area Code'],row['Country Code'],row['Detail'],row['Extension'], row['Integration Indicator'],row['List Item Index'],
                row['List Item Last Modified'],row['List Item Last Modified By'],row['Name'],row['Notes'],row['Position'],row['Preferred'],row['Preferred SMS Mobile'],
                row['Source'], row['Source Entity'],row['Source Index'],row['Type'],row['Unknown'],row['Update From Datafeed']
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

def update_entity(path):

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()


    # Read the CSV file into a df
    df = pd.read_csv(path, encoding='iso-8859-1')

    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    


    # Connect to the PostgreSQL database
    try:

        delete_all_query = """DELETE FROM entity;"""
        # Execute the DELETE statement
        cursor.execute(delete_all_query)


        # Iterate through the df and insert data into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO entity (entity_id, entity_name, category, entity_type, first_name, last_name, id, dob, age, marital_status, company_name, company_number, trust_name, 
            trust_number, offering, "subscription")
            VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)
            """
            cursor.execute(insert_query,(
                row['Entity Id'],row['Entity Name'],row['Category'],row['Entity Type'],row['First Name'],row['Surname'],row['ID'],row['Date of Birth'],row['Age'],
                row['Marital Status'],row['Company Name'],row['Company Number'],row['Trust Name'],row['Trust Number'],row['Offering'],row['Subscription'] 
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

def clear_tables():

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
  
    tables = ['contact','entity', 'epp', 'liaisons', 'reviews', 'tasks', 'referrers', 'staff', 'teams', 'wl']

    for table in tables:

        # Use table variable to specify the table name in the DELETE query
        delete_all_query = f"DELETE FROM {table};"
        # Execute the DELETE statement
        cursor.execute(delete_all_query)

    conn.commit()
    cursor.close()
    conn.close()





# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

update_TA(config_dev['Source']['TA'])
insert_liaison(config_dev['Source']['liaisons'])
insert_ror(config_dev['Source']['ror'])
insert_wl(config_dev['Source']['wl'])
insert_tasks(config_dev['Source']['tasks'])
insert_epp(config_dev['Source']['epp'])
update_referrers(config_dev['Source']['referrers'])
update_staff(config_dev['Source']['staff'])
update_entity(config_dev['Source']['entity'])
update_contact(config_dev['Source']['contact'])



# clear_tables()







#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

end_time = time.time()

seconds = end_time - start_time


h, m, s = map(lambda x: int(x), [seconds/3600, seconds%3600/60, seconds%60])

print(f'{h}:{m:02d}:{s:02d}')