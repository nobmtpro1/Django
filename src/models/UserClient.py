from django.db import models
from src.models.Course import Course
from src.models.Session import Session


class UserClient(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    has_sessions = models.ManyToManyField(Session)
    has_courses = models.ManyToManyField(Course)