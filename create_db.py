import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'baby_names'


def create_database():
	connection = psycopg2.connect( user=USERNAME, password=PASSWORD);
	connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
	cursor = connection.cursor();
	name_Database = "baby_names";
	sqlCreateDatabase = "create database "+name_Database+";"
	cursor.execute(sqlCreateDatabase);
	connection.close();

def create_table(table):
	connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE);
	cursor = connection.cursor()
	query = f'CREATE TABLE {table}( id SERIAL PRIMARY KEY, name VARCHAR (50) NOT NULL, rating INT)'
	cursor.execute(query)
	connection.commit()
	connection.close()





