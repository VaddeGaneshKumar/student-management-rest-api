from django import forms
from .models import Student

# Idi mana Form Design
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Ee form 'Student' table kosam
        fields = ['name', 'age', 'city']  # Ee columns kavali