#!/usr/bin/python3
"""List states"""

import MySQLdb
from sys import argv

# Prevent direct execution when imported
if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(argv)!= 5:
        print("Usage: python script.py <username> <password> <dbname> <state>")
        exit(1)

    # Extract arguments
    username, password, dbname, state = argv[1], argv[2], argv[3], argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Prepare the SQL query with placeholders for parameters
    query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC;"

    # Execute the query with the state name parameter
    cur.execute(query, (state,))

    # Fetch the result
    result = cur.fetchone()

    # Print the result
    if result:
        print(result[0])
    else:
        print("No cities found.")

    # Close the cursor and connection
    cur.close()
    db.close()
