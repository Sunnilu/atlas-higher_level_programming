#!/usr/bin/python3
"""Lists states"""

import MySQLdb
import sys

def list_states_starting_with_n(username, password, database):
    # Connect to MySQL server
    try:
        conn = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = conn.cursor()

        # Execute SQL query to retrieve states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        
        # Fetch all rows
        rows = cursor.fetchall()
        
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
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to list states starting with 'N'
    list_states_starting_with_n(username, password, database)

