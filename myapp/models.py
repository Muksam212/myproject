from django.db import models
from django.utils import timezone
# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	email=models.EmailField()
	date_created=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name