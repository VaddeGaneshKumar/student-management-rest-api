from rest_framework import serializers
from .models import Student # నీ దగ్గర Student అనే మోడల్ ఉందని అనుకుందాం

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'