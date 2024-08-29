from django.db import models
# Create your models here.
# class Eleve(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=100)
#     birth_date = models.DateField(null=True)
#     city = models.CharField(max_length=30, null=True)
#     number = models.CharField(max_length=10, null=True)
#     class_student = models.CharField(max_length=30, null=True)
#     register_number = models.CharField(max_length=30, null=True)

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    city = models.CharField(max_length=30, null=True)
    number = models.CharField(max_length=10, null=True)
    class_student = models.CharField(max_length=30, null=True)
    register_number = models.CharField(max_length=30, null=True)
    