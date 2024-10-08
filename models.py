from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)

class Projects(models.Model):
    project_title = models.CharField(max_length=100)
    description = models.TextField()
    project_url = models.URLField(blank=True)
from .models import PersonalInfo
