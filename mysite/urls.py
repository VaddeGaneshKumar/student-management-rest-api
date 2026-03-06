from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from core.models import Student
from core.forms import StudentForm

# 👇 1. కొత్తగా రాసిన మన API views ని ఇక్కడ import చేస్తున్నాం
from core import views as core_views

# 1. HOME VIEW (List chupinchadaniki)
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

# 2. ADD VIEW (Kotha student)
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})

# 3. DELETE VIEW
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(home)

# 4. UPDATE VIEW (Edit cheyadaniki)
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = StudentForm(instance=student)
    return render(request, 'update.html', {'form': form})

# URL PATTERNS
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home),  # Home Page
    path('add/', add_student),
    path('delete/<int:id>/', delete_student),
    path('update/<int:id>/', update_student),

    # 👇 2. ఇది మన కొత్త API URL! 
    path('api/students/', core_views.get_students),
    path('api/students/<int:pk>/', core_views.student_detail),
]