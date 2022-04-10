from dataclasses import field
from rest_framework import serializers
from .models import Student, Book

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'address']


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'publisher']