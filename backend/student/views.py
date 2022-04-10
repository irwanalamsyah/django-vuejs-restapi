from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student, Book
from .serializers import StudentSerializers, BookSerializers

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers