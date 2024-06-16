import mysql.connector

def connect_to_mysql():
'''
Establishes a connection to the MySQL database,

Returns:
    A mysql.connetor.MySQLConection object representing the connection to the MySQL server.
'''
cursor = cnx.cursor()

query = "SHOW DATABASES"

try:
cursor.execute(query)

for db in cursor:
	print(db[)])

finally:
   cursor.close()

if __name == "__main__":
	cnx = connect_to_mysql()
	if cnx:
		list_all_databases(cnx)
		cnx,close()
	else:
		print("Failed to establish a connection to the MySQL server.")
