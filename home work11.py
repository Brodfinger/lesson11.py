# from homework import Homework
import homework
from student import Student
from teacher import Teacher
from employee import Employye
from person import Person


#
# class Homework:
#
# 	def __init__(self, name, description, complexity, status):
# 		self.name = name
# 		self.description = description
# 		self.complexity = complexity
# 		self.status = status
# 		self.grade = 0
#
# 	def __str__(self):
# 		return f"{self.name}, {self.description}, {self.complexity}, {self.status}"

#
# class Course:
#     def __init__(self, name, description, student, teacher, date_start_course, date_end_course, num_lessons):
# 		self.name = name
# 		self.description = description
# 		self.student = student
# 		self.teacher = teacher
# 		self.date_start_course = date_start_course
# 		self.date_end_course = date_end_course
# 		self.num_lessons = num_lessons

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Teacher(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.course = []

# class Employye(Person):
#      def __init__(self, name, age):
#          super().__init__(name, age)
#          self.salary = 0



# class Student(Person):
# 	def __init__(self, surname, name, age, course):
# 		self.surname = surname
# 		self.name = name
# 		self.age = age
# 		self.avarage_grade = 0
# 		self.course = course
# 		self.homeworks = []
#
# 	def __str__(self):
# 		ret = f"surname: {self.surname}, name:{self.name}, age: {self.age}, grade: {self.avarage_grade}, course: {self.course}\n"
# 		ret = ret + "Homeworks:\n"
# 		for i in self.homeworks:
# 			ret = ret + "\t" + str(i) + "\n"
# 		return ret
#
# 	def add_homework(self, homework):
# 		self.homeworks.append(homework)

"""Sorted"""
"""Students"""
def show_students(students):
	for s in students:
		print(s)


def sort_by_name(students):
	return sorted(students, key=lambda s: s.name)

def sort_by_age(students):
	return sorted(students, key=lambda s: s.age)


def sort_by_grade(students):
	return sorted(students, key=lambda s: s.avarage_grade, reverse=True)

def sort_by_surname(students):
	return sorted(students, key=lambda s: s.surname)





"""Teachers"""
def show_teachers(teachers):
	for t in teachers:
		print(t)


def sort_by_name(teachers):
	return sorted(teachers, key=lambda t: t.name)

def sort_by_age(teachers):
	return sorted(teachers, key=lambda t: t.age)


def sort_by_surname(teachers):
	return sorted(teachers, key=lambda t: t.surname)

def sort_by_first_course(teachers):
	return sorted(teachers, key=lambda t: t.first_course)

def sort_by_second_course(teachers):
	return sorted(teachers, key=lambda t: t.second_course)

def sort_by_third_course(teachers):
	return sorted(teachers, key=lambda t: t.third_course)


"""Employee"""
def show_employye(employee):
	for e in employee:
		print(e)


def sort_by_name(employee):
	return sorted(employee, key=lambda e: e.name)

def sort_by_age(employee):
	return sorted(employee, key=lambda e: e.age)


def sort_by_surname(employee):
	return sorted(employee, key=lambda e: e.surname)

"""Staff"""
teachers = [
	Teacher("Hon", "Smith", 35, "C++", "Python", "Don't have"),
	Teacher("Tirner", "Alex", 36, "Java", "C++", "Python")
]
employee =[
	Employye("Smith", "Leo", 27)
]
"""Visitors"""
students = [
	Student("Smith", "Lena", 18, "C++"),
	Student("Williams", "Nike", 26, "Python"),
	Student("Brown", "Peter", 25, "Java"),
	Student("Smith", "John", 15, "Python"),
	Student("Wilson", "Peter", 17, "C++"),
	Student("Key", "Nik", 14, "Python"),
	Student("Li", "Theo", 17, "Java"),
	Student("Lifo", "Joa", 19, "C++"),
	Student("Hernandez", "Teo", 24, "Python"),
	Student("Orlov", "Dima", 16, "Java")



]

homeworks = [
	homework("Homework 1", "Description 1", 2, False),
	homework("Homework 2", "Description 2", 5, False)
]

print("Initial")
show_students(students)
print("Sorted by name")
show_students(sort_by_name(students))
print("Sorted by surname")
show_students(sort_by_surname(students))
print("Sorted by age")
show_students(sort_by_age(students))
print("Sorted by grade")
show_students(sort_by_grade(students))


print("Initial")
show_teachers(teachers)
print("Sorted by name")
show_teachers(sort_by_name(teachers))
print("Sorted by surname")
show_teachers(sort_by_surname(teachers))
print("Sorted by age")
show_teachers(sort_by_age(teachers))
print("Sorted by First_course")
show_teachers(sort_by_first_course(teachers))
print("Sorted by Second_course")
show_teachers(sort_by_second_course(teachers))
print("Sorted by Third_course")
show_teachers(sort_by_third_course(teachers))




print("Initial")
show_employye(employee)
print("Sorted by name")
show_employye(sort_by_name(employee))
print("Sorted by surname")
show_employye(sort_by_surname(employee))
print("Sorted by age")
show_employye(sort_by_age(employee))

print(homework.__doc__)
print(homework.Homework.__doc__)


