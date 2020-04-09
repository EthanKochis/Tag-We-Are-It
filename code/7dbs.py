#! /usr/bin/python2

"""
IMPORTANT

To run this example in the CSC 315 VM you first need to make
the following one-time configuration changes:

# install psycopg2 python package
sudo apt-get update
sudo apt-get install postgres-psycopg2

# set the postgreSQL password for user 'osc'
sudo -u postgres psql
    ALTER USER osc PASSWORD 'osc';
    \q
"""

"""
CSC 315
Spring 2020
John DeGood

Usage:
python2 7dbs.py 

Purpose:
Demonstrate Python connection to PostgreSQL using the psycopg
adapter. Connects to the 7dbs database from "Seven Databases
in Seven Days" in the CSC 315 VM.

This example uses Python 2 because Python 2 is the default in
Ubuntu 18.04 LTS on the CSC 315 VM.

For psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
"""

import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % params['database'])
        conn = psycopg2.connect(**params)
        print('Connected.\n')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('PostgreSQL version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version[0])
       
        # execute a query using fetchall()
        print('\nPostgreSQL SELECT result (sorted by country_code):')
        cur.execute("SELECT country_code, country_name FROM countries ORDER BY country_code")
        rows = cur.fetchall()
        print('The number of countries: %d' % cur.rowcount)
        for row in rows:
            print('%s\t%s' % (row[0], row[1]))

       # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('\nDatabase connection closed.')
 
if __name__ == '__main__':
    connect()
