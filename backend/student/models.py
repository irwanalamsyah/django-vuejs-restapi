from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name 


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.name 