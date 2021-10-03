# Author: Danilo Nascimento
# Contact: ndanilo8@hotmail.com
# Description: This is the database handler for the Race Strategy creation. It's written with Python and relies on the SQLite3 DB

# Based of the google sheets stint calculator https://docs.google.com/spreadsheets/d/1xvdXoQC3cvjysds_nth3MmrK9AnR3qjD-pyy-22ukHE/edit?usp=sharing


import sqlite3

# Create a Table


def create_tables():
    # Connect to database
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE raceInfo (
            track_name TEXT,
            race_length TEXT,
            race_date TEXT,
            driver_briefing_time TEXT,
            qualifying_time TEXT,
            warmup_time TEXT,
            race_time TEXT,
            maximum_cut_tracks TEXT
        )""")

    # Fixed Table with different cars data
    c.execute("""CREATE TABLE carData (
            class TEXT,
            car_name TEXT,
            fuel_tank_size_in_liters REAL,
            pit_stop_time_in_seconds REAL
        )""")

    # Stints Table that differs from race to race
    c.execute("""CREATE TABLE stintInfo (
            laptime TEXT,
            fuel_per_lap REAL,
            tire_wear_per_lap REAL,
            fuel_range_in_laps REAL,
            no_of_refuels INTEGER,
            tyre_range INTEGER,
            no_of_tyre_changes INTEGER,
            swap_at_percentage INTEGER,
            tyres_every INTEGER,
            tyres_constant INTEGER,
            fuel_per_race_in_liters REAL,
            avg_refuel_in_liters REAL,
            avg_stint_laps REAL,
            last_pit_lap INTEGER,
            fuel_splash_in_liters INTEGER
        )""")

    c.execute("""CREATE TABLE pitTimeLost (
           refuelSpeed_in_seconds REAL,
           fuel_per_hour REAL,
           time_lost_total REAL,
           time_tyres REAL,
           tread_per_hour REAL,
           time_lost_total REAL,
           time_coeff REAL
        )""")

    c.execute("""CREATE TABLE drivers (
            first_name TEXT,
            last_name TEXT,
            email TEXT
        )""")

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# TODO we have more than one table 
# Query the DB and return all records
def show_all():
    # Connect to database
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM raceInfo")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

    # Add a new record to the table

# TODO we have more than one table 
def add_one_record(first_name, last_name, email):
    # Connect to database
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO raceInfo VALUES (?,?,?)",
              (first_name, last_name, email))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

# Add Many Records To Table


# TODO we have more than one table 
def add_many_records(List):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.executemany("INSERT INTO raceInfo VALUES (?,?,?)", (List))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

# TODO we have more than one table 
# Delete Record from Table
def delete_one_record(id):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE from raceInfo WHERE rowid = (?)", id)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# gotta write this
# TODO we have more than one table 
def delete_all_tables():
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE TABLE ")
   
    # commit out command
    conn.commit()   

    items = c.fetchall()

    for item in items:
        print(item)

    # close our connection
    conn.close()
