from django.contrib import admin
from .models import Student

# Students table ni Admin panel lo chupinchu
admin.site.register(Student)