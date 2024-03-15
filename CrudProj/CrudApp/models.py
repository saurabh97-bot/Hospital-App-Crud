from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    admitted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Patient name is {self.name}"
