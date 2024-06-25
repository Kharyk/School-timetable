from django.contrib import admin
from .models import Class, Student, Subject, Teacher, Schadule,Students_to_subject, Teacher_to_subject
#proxymodelapp
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Schadule)
admin.site.register(Students_to_subject)
admin.site.register(Teacher_to_subject)



