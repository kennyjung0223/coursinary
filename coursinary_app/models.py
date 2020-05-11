from django.db import models
from django.utils import timezone

class Subject(models.Model):
	"""Subject of a particular course"""
	text = models.CharField(max_length=50)
	code = models.CharField(max_length=10)

	def __str__(self):
		"""Return a string representation of a model"""
		return self.text

class Course(models.Model):
	"""Particular course"""
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	text = models.CharField(max_length=60)
	code = models.CharField(max_length=10)
	course_number = models.CharField(max_length=5)

	class Meta:
		verbose_name_plural = 'courses'

	def __str__(self):
		"""Return a string representation of the model"""
		return self.text

class Entry(models.Model):
	"""Entry that explains more about a particular course"""
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model"""
		if len(self.text) < 50:
			return self.text
		return f"{self.text[:50]}..."