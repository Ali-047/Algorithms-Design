from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Student(AbstractUser):
    national_id = models.CharField(max_length=10, unique=True)
    student_id = models.CharField(max_length=8,unique=True)




