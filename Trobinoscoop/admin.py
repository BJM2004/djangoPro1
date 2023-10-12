from django.contrib import admin
from .models import Faculty, Cursus, Campus, Message, Employee, Job, Student
admin.site.register(Faculty)
admin.site.register(Campus)
admin.site.register(Job)
admin.site.register(Cursus)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Message)
