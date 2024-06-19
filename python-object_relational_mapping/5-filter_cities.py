#!/usr/bin/python3
"""List states"""

import MySQLdb
from sys import argv

def list_cities_by_state(username, password, dbname, state):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=dbname)
        cur = db.cursor()

        # Prepare the SQL query with placeholders for parameters
        query = """
            SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') 
            FROM cities 
            INNER JOIN states ON cities.state_id = states.id 
            WHERE states.name = %s 
            ORDER BY cities.id ASC
        """

        # Execute the query with the state name parameter
        cur.execute(query, (state,))

        # Fetch the result
        result = cur.fetchone()

        # Handle the case where no cities were found
        if result and result[0]:
            print(result[0])
        else:
            print("")  # Print an empty string to match the expected output length for "Empty"

        # Close the cursor and connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        exit(1)

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(argv) != 5:
        print("Usage: python script.py <username> <password> <dbname> <state>")
        exit(1)

    # Extract arguments
    username, password, dbname, state = argv[1], argv[2], argv[3], argv[4]

    # Call function to list cities by state
    list_cities_by_state(username, password, dbname, state)
