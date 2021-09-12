"""Class Course"""
class Course:
    """Course class"""
    def __init__(self, name, description, student, teacher, date_start_course, date_end_course, num_lessons):
		"""Some doc"""
		self.name = name
		self.description = description
		self.student = student
		self.teacher = teacher
		self.date_start_course = date_start_course
		self.date_end_course = date_end_course
		self.num_lessons = num_lessons
	def _str_(self):
		return f"Information about course - (name, description, student, teacher, date_start_course, date_end_course, num_lessons)"