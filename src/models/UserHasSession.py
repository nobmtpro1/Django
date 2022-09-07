from django.db import models
from .Session import Session
from .UserClient import UserClient


class UserHasSession(models.Model):
    user_client = models.ForeignKey(UserClient, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
