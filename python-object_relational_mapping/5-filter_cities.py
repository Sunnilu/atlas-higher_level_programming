#!/usr/bin/python3
"""List states"""


import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = conn.cursor()

        # Prepare SQL query with parameterized query
        query = """
            SELECT cities.id, cities.name 
            FROM cities 
            JOIN states ON cities.state_id = states.id 
            WHERE states.name = %s 
            ORDER BY cities.id ASC
        """
        
        # Execute query with parameter safely
        cursor.execute(query, (state_name,))

        # Fetch all rows
        rows = cursor.fetchall()

        if not rows:
            print(f"No cities found for state '{state_name}'")
        else:
            # Print results as specified
            for row in rows:
                print(row)

        # Close cursor and connection
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get MySQL credentials, database name, and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call function to list cities by state
    list_cities_by_state(username, password, database, state_name)
