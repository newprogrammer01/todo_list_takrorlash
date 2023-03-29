from django.contrib import admin

# Register your models here.
from .moduls import Task, Student
admin.site.register([Task, Student])

