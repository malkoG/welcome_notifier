from django.db import models

# Create your models here.
class Member(models.Model):
    name         = models.CharField(max_length=30, blank=False)
    student_id   = models.CharField(max_length=20, blank=False, unique=True)
    phone_number = models.CharField(max_length=30, blank=False)
    email        = models.CharField(max_length=100, blank=False)

class Template(models.Model):
    name = models.CharField(max_length=30, blank=False)
    text = models.TextField(blank=False)
