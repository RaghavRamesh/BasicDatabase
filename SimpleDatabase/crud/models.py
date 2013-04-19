from django.db import models

# Create your models here.
class Employee(models.Model):
	empno = models.CharField(max_length=10)
	ename = models.CharField(max_length=20)
	job = models.CharField(max_length=20)
	salary = models.IntegerField(max_length=10)