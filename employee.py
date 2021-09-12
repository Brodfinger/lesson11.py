"""Class Person"""
from person import Person
"""Class Employye"""
class Employye(Person):
    """Employye class"""
    def __init__(self,surname, name, age):
        """Some class"""
        super().__init__(surname,name, age)
        self.salary = 0

    def _str_(self):
        return f"Information about employee - (surname,name, age)"