import menu
import create_db
from faker import Faker 
fake = Faker()

# create_db.if_db_exists()
# create_db.create_database()
# create_db.create_table()

print('Congratulations on the birth of your child!\n')
gender = input("If it's a boy type boy, if a girl type girl: ")

#################################################################


def no_length():
	m1 = menu.Menu()
	while True:
		if gender == 'boy':
			new_name = fake.first_name_male()
		else:
			new_name = fake.first_name_female()
		print(new_name)
		user_like = input("if you like this name type yes, else type no: ")
		if user_like == 'yes':
			menu.insert(new_name)
			m1.choice()

		else:
			m1.choice()


def with_max_length():
	m2 = menu.Menu()
	length = int(input('Max length of name: '))
	while True:
		if gender == 'boy':
			while True:
				new_name = fake.first_name_male()
				if len(new_name) <= length:
					break;
		else:
			while True:
				new_name = fake.first_name_female()
				if len(new_name) <= length:
					break;
		print(new_name)
		user_like = input("if you like this name type yes, else type no: ")
		if user_like == 'yes':
			menu.insert(new_name)
			m2.choice()

		else:
			m2.choice()


#######################################################


user_choice = input('Would you like to set a max length for the name? (yes/no) ')
if user_choice == 'yes':
	with_max_length()
else:
	no_length()

		


