import menu
import jewish_boys as jb
import jewish_girls as jg
import popular_boys as pb
import popular_girls as pg
from faker import Faker 
fake = Faker()


class Babies():

	def __init__(self, gender):
		self.gender = gender

	def just_name(self):
		m1 = menu.Menu('just_name')
		while True:
			if self.gender == 'boy':
				new_name = fake.first_name_male()
			else:
				new_name = fake.first_name_female()
			print(new_name)
			user_like = input("if you like this name type yes, else type no: ")
			if user_like == 'yes':
				m1.insert(new_name)
				m1.choice()

			else:
				m1.choice()


	def with_max_length(self):
		m2 = menu.Menu('max')
		length = int(input('Max length of name: '))
		while True:
			if self.gender == 'boy':
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
				m2.insert(new_name)
				m2.choice()

			else:
				m2.choice()

	def with_first_letter(self):
		m3 = menu.Menu('first')
		first_letter = input('First letter of name: ').upper()
		while True:
			if self.gender == 'boy':
				while True:
					new_name = fake.first_name_male()
					list_name = new_name.split()
					if list_name[0][0] == first_letter:
						break;
			else:
				while True:
					new_name = fake.first_name_female()
					list_name = new_name.split()
					if list_name[0][0] == first_letter:
						break;
			print(new_name)
			user_like = input("if you like this name type yes, else type no: ")
			if user_like == 'yes':
				m3.insert(new_name)
				m3.choice()

			else:
				m3.choice()

	def max_and_first(self):
		m4 = menu.Menu('max_and_first')
		first_letter = input('First letter of name: ').upper()
		length = int(input('Max length of name: '))
		while True:
			if self.gender == 'boy':
				while True:
					new_name = fake.first_name_male()
					list_name = new_name.split()
					if list_name[0][0] == first_letter:
						if len(new_name) <= length:
							break;
			else:
				while True:
					new_name = fake.first_name_female()
					list_name = new_name.split()
					if list_name[0][0] == first_letter:
						if len(new_name) <= length:
							break;
			print(new_name)
			user_like = input("if you like this name type yes, else type no: ")
			if user_like == 'yes':
				m4.insert(new_name)
				m4.choice()

			else:
				m4.choice()



	def jewish(self):
		while True:
			if self.gender == 'boy':
				m5 = menu.Menu('jewish_boys_names')
				jb.main()
				m5.view()
				m5.choice()
			else:
				m6 = menu.Menu('jewish_girls_names')
				jg.main()
				m6.view()
				m6.choice()

	def popular_names(self):
		while True:
			if self.gender == 'boy':
				m7 = menu.Menu('popular_boys_names')
				pb.main()
				m7.view()
				m7.choice()
			else:
				m8 = menu.Menu('popular_girls_names')
				pg.main()
				m8.view()
				m8.choice()

