from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=204)


    def __str__(self):
        return self.name
