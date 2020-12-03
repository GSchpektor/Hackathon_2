from bs4 import BeautifulSoup
import requests
import re
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'baby_names'


res = requests.get("https://www.familyeducation.com/baby-names/popular-names/boys")
html = res.text

soup = BeautifulSoup(html)
for node in soup.findAll(id="block-boytopnames"):
	temp_names = ''.join(node.findAll(text=True))
	names = re.sub (r'([^a-zA-Z\s]+?)', '', temp_names).split("\n")
	

def create_table():
	connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE);
	cursor = connection.cursor()
	query = 'CREATE TABLE popular_boys_names( id SERIAL PRIMARY KEY, name VARCHAR (50) NOT NULL, rating INT)'
	cursor.execute(query)
	connection.commit()
	connection.close()


def insert():
	connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
	cursor = connection.cursor()
	for name in names:
		query = f"INSERT INTO popular_boys_names (name) VALUES ('{name.strip()}');"
		cursor.execute(query)
		connection.commit()
	connection.close()


def main():
	create_table()
	insert()





