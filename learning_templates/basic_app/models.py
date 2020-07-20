from django.db import models
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=264)
    rollnumber=models.IntegerField(unique=True)
    batch=models.CharField(max_length=264)
