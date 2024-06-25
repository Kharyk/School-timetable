from table import models
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

django.setup()

from table.models import Teacher, Class, Subject, Student, Students_to_subject, Schadule, Teacher_to_subject


teachers = [Teacher(first_name = "Nadiia", surname = "Luhova", email = "nadiia543@gmail.com"),
            Teacher(first_name = "Ivan", surname = "Ostapchuk", email = "ivan7584@gmail.com"),
            Teacher(first_name = "Alina", surname = "Kharyk", email = "alina987@gmail.com"),
            Teacher(first_name = "Max", surname = "Kupchuk", email = "max675@gmail.com")]
Teacher.objects.bulk_create(teachers)

classes = [Class(numder_of_class = 4),
           Class(numder_of_class = 5),
           Class(numder_of_class = 29),
           Class(numder_of_class = 28),
           Class(numder_of_class = 34),
           Class(numder_of_class = 35)]
Class.objects.bulk_create(classes)

subjects = [Sudject(name = "math", curator = "Lidia"),
            Sudject(name = "english", curator = "Oleksiu"),
            Sudject(name = "history", curator = "Ostap")]
Subject.objects.bulk_create(subjects)

students = [Student(first_name='Sovia', surname= "Popovuch", email= "sovia987@gmail.com"),
           Student(first_name='Marta', surname= "Kerush", email= "martaa87@gmail.com"),
           Student(first_name='Bogdan', surname= "Andriiv", email= "bogdan07@gmail.com"),
           Student(first_name='Veronika', surname= "Nauvak", email= "verooonichra@gmail.com")]
Student.objects.bulk_create(students)

stTOsub = [Students_to_subject(student=1, subject=2),
           Students_to_subject(student=1, subject=3),
           Students_to_subject(student=2, subject=1),
           Students_to_subject(student=3, subject=2),
           Students_to_subject(student=3, subject=3),
           Students_to_subject(student=4, subject=1),
           Students_to_subject(student=4, subject=2)]
Students_to_subject.objects.bulk_create(stTOsub)

schadules = [Schadule(time = "08:30", subject = 1, id_class= 3),
             Schadule(time = "10:30", subject = 2, id_class= 6),
             Schadule(time = "12:30", subject = 3, id_class= 1)]
Schadule.objects.bulk_create(schadules)

teaTOsub = [Teacher_to_subject(teacher = 1, subject = 2),
            eacher_to_subject(teacher = 2, subject = 1),
            eacher_to_subject(teacher = 2, subject = 3),
            eacher_to_subject(teacher = 3, subject = 2),
            eacher_to_subject(teacher = 4, subject = 2),
            eacher_to_subject(teacher = 4, subject = 1)]
Teacher_to_subject.objects.bulk_create(teaTOsub)

teachers = Teacher.objects.all()

print("Teachers List:")
print("-" * 30)

for teacher in teachers:
    print(f"Name: {teacher.first_name} {teacher.surname}")
    print(f"Email: {teacher.email}")
    print("-" * 30)