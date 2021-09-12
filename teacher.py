"""Class Person"""
from person import Person
"""Class Teacher"""
class Teacher(Person):
    """Teacher class"""
    def __init__(self, surname, name, age, first_course, second_course, third_course):
        """Some doc"""
        super().__init__(surname, name, age, first_course, second_course, third_course)
        self.course = []

    def _str_(self):
        return f"Information about teacher - (surname, name, age, first_course, second_course, third_course)"