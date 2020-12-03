import menu
import create_db
import options
from faker import Faker 
fake = Faker()

# use the functions below to create a db, 
# it requires the name and password to be set to postgres
# create_db.create_database()


print('Congratulations on the birth of your child!\n')

gender = input("If it's a boy type boy, if a girl type girl: ").lower()

user_choice = input("""Would you like to:\n
set a max length for the name? (max)\n
choose a first letter? (first)\n
both (both)\n
see a list of popular boys names (pn)\n
see a list of jewish names (jn)\n
or (any)?  """).lower()

if user_choice == 'max':
	create_db.create_table('max')
	b1 = options.Babies(gender)
	b1.with_max_length()
elif user_choice == 'first':
	create_db.create_table('first')
	b2 = options.Babies(gender)
	b2.with_first_letter()
elif user_choice == 'both':
	create_db.create_table('max_and_first')
	b3 = options.Babies(gender)
	b3.max_and_first()
elif user_choice == 'pn':
	b4 = options.Babies(gender)
	b4.popular_names()
elif user_choice == 'jn':
	b5 = options.Babies(gender)
	b5.jewish()
else:
	create_db.create_table('just_name')
	b6 = options.Babies(gender)
	b6.just_name()

		


