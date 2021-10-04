# Author: Danilo Nascimento
# Contact: ndanilo8@hotmail.com
# Description: This is the database handler for the Race Strategy creation. It's written with Python and relies on the SQLite3 DB

# Based of the google sheets stint calculator https://docs.google.com/spreadsheets/d/1xvdXoQC3cvjysds_nth3MmrK9AnR3qjD-pyy-22ukHE/edit?usp=sharing


import sqlite3

# Create Tables
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
            maximum_cut_tracks TEXT,
            raceView TEXT,
            weather_forecast TEXT,
            incident_report_form TEXT,
            driver_change_form TEXT
        )""")

    # Commit our command
    conn.commit()

    # Fixed Table with different cars data
    c.execute("""CREATE TABLE carData (
            class TEXT,
            car_name TEXT,
            fuel_tank_size_in_liters REAL,
            pit_stop_time_in_seconds REAL
        )""")

    # Commit our command
    conn.commit()

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

    # Commit our command
    conn.commit()

    c.execute("""CREATE TABLE pitTimeLost (
           refuelSpeed_in_seconds REAL,
           fuel_per_hour REAL,
           time_lost_total_fuel REAL,
           time_tyres REAL,
           tread_per_hour REAL,
           time_lost_total_tyre REAL,
           time_coeff REAL
        )""")

    # Commit our command
    conn.commit()

    c.execute("""CREATE TABLE drivers (
            first_name TEXT,
            last_name TEXT,
            email TEXT
        )""")

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

# Query the DB and return all records
def show_all():
    # Connect to database
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # Query the database    
    c.execute("SELECT rowid, * FROM raceInfo")
    raceInfoTable = c.fetchall()
    # print if records exist
    if raceInfoTable: 
        print("Race Info Table")
    for item in raceInfoTable:
        print(item)
    
    # Query the database 
    c.execute("SELECT rowid, * FROM carData")
    carDataTable = c.fetchall()
    # print if records exist
    if carDataTable:
        print("Car Data Table")
    for item in carDataTable:
        print(item)

    # Query the database 
    c.execute("SELECT rowid, * FROM pitTimeLost")
    pitTimeLostTable = c.fetchall()
    # print if records exist
    if pitTimeLostTable:
        print("Pit Time Lost Table") 
    for item in pitTimeLostTable:
        print(item)
    
    # Query the database 
    c.execute("SELECT rowid, * FROM drivers")
    driversTable = c.fetchall()
    # print if records exist
    if driversTable:
        print("Drivers Table")
    for item in driversTable:
        print(item)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

# Add a new record to the pitTimelost table
def add_one_pitTimelost_record(refuel_speed_in_seconds, fuel_per_hour, time_lost_total_fuel,time_tyres,tread_per_hour, time_lost_total_tyre, time_coeff):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO pitTimeLost VALUES (?,?,?,?,?,?,?)",
              (refuel_speed_in_seconds, fuel_per_hour, time_lost_total_fuel,time_tyres,tread_per_hour, time_lost_total_tyre, time_coeff))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

# Add a Record to the drivers Table
def add_one_driver_record(first_name, last_name, email):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO drivers VALUES (?,?,?)",
              (first_name, last_name, email))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Add a Record to carData Table
def add_one_carData_record(car_class, car_name, fuel_tank_size, pit_stop_time_in_seconds):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO carData VALUES (?,?,?,?)",
              (car_class, car_name, fuel_tank_size, pit_stop_time_in_seconds))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

def add_one_raceInfo_record(track_name, race_length, race_date, driver_briefing_time,qualifying_time,warmup_time,race_time,maximum_cut_tracks,raceView,weather_forecast,incident_report_form,driver_change_form):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO raceInfo VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
              (track_name, race_length, race_date, driver_briefing_time,qualifying_time,warmup_time,race_time,maximum_cut_tracks,raceView,weather_forecast,incident_report_form,driver_change_form))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Add a Record to carData Table
def add_one_carData_record(car_class, car_name, fuel_tank_size, pit_stop_time_in_seconds):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO carData VALUES (?,?,?,?)",
              (car_class, car_name, fuel_tank_size, pit_stop_time_in_seconds))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()

# Add a Record to carData Table
def add_one_stintInfo_record(laptime, fuel_per_lap, tire_wear_per_lap, fuel_range_in_laps,no_of_refuels,tyre_range,no_of_tyre_changes,swap_at_percentage,tyres_every,tyres_constant,fuel_per_race_in_liters,avg_refuel_in_liters,avg_stint_laps,last_pit_lap,fuel_splash_in_liters):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO stintInfo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (laptime, fuel_per_lap, tire_wear_per_lap, fuel_range_in_laps,no_of_refuels,tyre_range,no_of_tyre_changes,swap_at_percentage,tyres_every,tyres_constant,fuel_per_race_in_liters,avg_refuel_in_liters,avg_stint_laps,last_pit_lap,fuel_splash_in_liters))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# TODO
# Add Many Records To a Table
def add_many_records(List):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.executemany("INSERT INTO raceInfo VALUES (?,?,?)", (List))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Delete one record from a table
def delete_one_record(id, table_name):
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    sql_command = "DELETE from " + table_name + " WHERE rowid = (?)"
    c.execute(sql_command, id)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# delete all tables   
def delete_all_tables():
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("DROP TABLE carData")
    # commit out command
    conn.commit()   

    c.execute("DROP TABLE drivers")
    # commit out command
    conn.commit()

    c.execute("DROP TABLE pitTimeLost")
    # commit out command
    conn.commit()

    c.execute("DROP TABLE raceInfo")
    # commit out command
    conn.commit()   
    
    c.execute("DROP TABLE stintInfo")
    # commit out command
    conn.commit()

    # close our connection
    conn.close()

# Delete only one table   
def delete_one_table(table_name):
    command = "DROP TABLE " + table_name
    # Connect to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute(command)
    # commit out command
    conn.commit()   

    # close our connection
    conn.close()