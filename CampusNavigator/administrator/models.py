from django.db import models

# Create your models here.
class Subjects (models.Model):
    Subject = models.CharField(max_length=30)
    Professor = models.CharField(max_length=30)
    Day = models.CharField(max_length=15)
    Time = models.CharField(max_length=15)
    Credits = models.IntegerField(null=True, blank=True)
class Enroll_subjects(models.Model):
    Subject = models.CharField(max_length=30)
    Professor = models.CharField(max_length=30)
    Credits = models.IntegerField(null=True, blank=True)