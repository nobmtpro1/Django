from django.db import models
from .Course import Course
from .UserClient import UserClient


class UserHasCourse(models.Model):
    user_client = models.ForeignKey(UserClient, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
