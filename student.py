"""Class Person"""
from person import Person
"""Class Student"""
class Student(Person):
	"""Student Class"""
	def __init__(self, surname, name, age, course):
		"""Some doc"""
		self.surname = surname
		self.name = name
		self.age = age
		self.avarage_grade = 0
		self.course = course
		self.homeworks = []
		"""Table"""
	def __str__(self):
		ret = f"surname: {self.surname}, name:{self.name}, age: {self.age}, grade: {self.avarage_grade}, course: {self.course}\n"
		ret = ret + "Homeworks:\n"
		for i in self.homeworks:
			ret = ret + "\t" + str(i) + "\n"
		return ret

	def add_homework(self, homework):
		self.homeworks.append(homework)
	def _str_(self):
		return f"Information about student - (surname, name, age, course)"
