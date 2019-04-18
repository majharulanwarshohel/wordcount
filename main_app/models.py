from django.db import models

# Create your models here.


class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    studentId = models.CharField(max_length=100)

    def __str__(self):
        return self.studentId


class Parents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    fatherCell = models.CharField(max_length=20)
    fatherEmail = models.CharField(max_length=50)
    motherCell = models.CharField(max_length=20)
    motherEmail = models.CharField(max_length=50)
    presentAddress = models.CharField(max_length=200)
    permanentAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.fatherName
