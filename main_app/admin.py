from django.contrib import admin

from .models import Student
from .models import Parents

admin.site.register(Student)
admin.site.register(Parents)
