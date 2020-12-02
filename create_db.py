import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'baby_names'

# def if_db_exists():
# 	connection = None
# 	try:
# 		connection = psycopg2.connect("user='postgres' host='localhost' password='postgres' port='5432'")
#     	print('Database connected.')
#     except:
#     	print('Database not connected.')

# 	if connection is not None:
# 	    connection.autocommit = True

# 	    cur = connection.cursor()

# 	    cur.execute("SELECT datname FROM pg_database;")

# 	    list_database = cur.fetchall()

# 	    database_name = input('Enter database name to check exist or not: ')

#     if (database_name,) in list_database:
#         print("'{}' Database already exist".format(database_name))
#     else:
#         print("'{}' Database not exist.".format(database_name))
#     connection.close()
#     print('Will create database now...')





def create_database():
	connection = psycopg2.connect( user=USERNAME, password=PASSWORD);
	connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
	cursor = connection.cursor();
	name_Database = "baby_names";
	sqlCreateDatabase = "create database "+name_Database+";"
	cursor.execute(sqlCreateDatabase);
	connection.close();

def create_table():
	connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE);
	cursor = connection.cursor()
	query = 'CREATE TABLE baby_names( id SERIAL PRIMARY KEY, name VARCHAR (50) NOT NULL, rating INT)'
	cursor.execute(query)
	connection.commit()
	connection.close()



