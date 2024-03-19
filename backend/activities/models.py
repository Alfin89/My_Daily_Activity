from django.db import models

# Create your models here.
class Activity(models.Model):
    activityId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
