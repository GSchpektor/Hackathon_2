import pandas
import pandas.io.sql as psql
import psycopg2


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
		df = psql.read_sql("SELECT name, rating FROM baby_names", connection)
		print(df)
		self.choice()

	def internal_view(self):
		connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
		cursor = connection.cursor()
		df = psql.read_sql("SELECT name, rating FROM baby_names", connection)
		print(df)

	def rate(self):
		self.internal_view()
		name_to_rate = input('which name would you like to rate? ')
		rating = input('What rating would you like to give it? ')
		query = f"UPDATE baby_names SET rating = {rating} WHERE name = '{name_to_rate}'"
		execute(query)
		self.choice()

	def delete(self):
		self.internal_view()
		name_to_delete = input('which name would you like to delete? ')
		query = f"DELETE FROM baby_names WHERE name = '{name_to_delete}'"
		execute(query)
		self.choice()

	def delete_all(self):
		query = f"DELETE FROM baby_names"
		execute(query)
		self.choice()


	def export(self):
		connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
		cursor = connection.cursor()
		df = psql.read_sql("SELECT name, rating FROM baby_names", connection)
		with open("index.html", "w") as f:
			f.write(df.to_html())
		exit()


def insert(name):
	query = f"INSERT INTO baby_names (name) VALUES ('{name}');"
	execute(query)


