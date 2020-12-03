import pandas as pd
import pandas.io.sql as psql
import numpy as np
import psycopg2
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)





HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'baby_names'



def execute(query):
	connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
	cursor = connection.cursor()
	cursor.execute(query)
	connection.commit()
	connection.close()



class Menu:

	def __init__(self, table):
		self.table = table


	def choice(self):
		menu_choice = input("Would you like to (v)iew, (g)enerate, (r)ate, (d)elete, delete (a)ll or (e)xport and quit? ")
		if menu_choice == 'v':
			self.view()
		elif menu_choice == 'g':
			return True
		elif menu_choice == 'r':
			self.rate()
		elif menu_choice == 'd':
			self.delete()
		elif menu_choice == 'a':
			self.delete_all()
		elif menu_choice == 'e':
			self.export()
		else:
			self.exit()

	def view(self):
		connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
		cursor = connection.cursor()
		df = psql.read_sql(f"SELECT name, rating FROM {self.table}", connection)
		df['name'] = df['name'].str.rstrip()
		print(df)
		self.choice()

	def internal_view(self):
		connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
		cursor = connection.cursor()
		df = psql.read_sql(f"SELECT name, rating FROM {self.table}", connection)
		print(df)

	def rate(self):
		self.internal_view()
		name_to_rate = input('which name would you like to rate? ')
		rating = input('What rating would you like to give it? ')
		query = f"UPDATE {self.table} SET rating = {rating} WHERE name = '{name_to_rate}'"
		df['name'] = df['name'].str.rstrip()
		execute(query)
		self.choice()

	def delete(self):
		self.internal_view()
		name_to_delete = input('which name would you like to delete? ')
		query = f"DELETE FROM {self.table} WHERE name = '{name_to_delete}'"
		execute(query)
		self.choice()

	def delete_all(self):
		query = f"DELETE FROM {self.table}"
		execute(query)
		self.choice()


	def export(self):
		connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
		cursor = connection.cursor()
		df = psql.read_sql(f"SELECT name, rating FROM {self.table}", connection)
		df['name'] = df['name'].str.rstrip()
		with open("index.html", "w") as f:
			f.write(df.to_html())
		exit()


	def insert(self, name):
		query = f"INSERT INTO {self.table} (name) VALUES ('{name}');"
		execute(query)


