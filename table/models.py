from django.db import models
#from django.db.models import Model

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length = 100)
    #date_of_start_of_work = models.DateField()
    email = models.EmailField(max_length=254)
    
class Class(models.Model):
    numder_of_class = models.CharField(max_length = 50)
    
class Subject(models.Model):
    name = models.CharField(max_length=250)
    curator = models.CharField(max_length=150)
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    #birthday = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField( max_length=254)
    
class Students_to_subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Schadule(models.Model):
    #day_of_the_week = models.DataField()
    time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    id_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    
class Teacher_to_subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


