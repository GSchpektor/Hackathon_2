import pandas
import pandas.io.sql as psql
import requests
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'baby_names'



	

def create_table():
	connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE);
	cursor = connection.cursor()
	query = 'CREATE TABLE jewish_boys_names( id SERIAL PRIMARY KEY, name VARCHAR (50) NOT NULL, rating INT)'
	cursor.execute(query)
	connection.commit()
	connection.close()


def insert():
	connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
	cursor = connection.cursor()
	with open('j_boys.txt', 'r') as f:
		for name in f:
			query = f"INSERT INTO jewish_boys_names (name) VALUES ('{name.rstrip()}');"
			cursor.execute(query)
			connection.commit()
	connection.close()




def main():
	create_table()
	insert()




 




