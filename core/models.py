from django.db import models

# Ide mana Database Table!
class Student(models.Model):
    name = models.CharField(max_length=100)  # Peru (Text)
    age = models.IntegerField()              # Vayasu (Number)
    city = models.CharField(max_length=100)  # Ooru (Text)

    def __str__(self):
        return self.name