"""class Homework"""
class Homework:
	"""Home work class"""
	def __init__(self, name, description, complexity, status):
		"""Some doc"""
		self.name = name
		self.description = description
		self.complexity = complexity
		self.status = status
		self.grade = 0

	def __str__(self):
		return f"{self.name}, {self.description}, {self.complexity}, {self.status}"