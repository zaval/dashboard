from django.contrib.postgres.fields import HStoreField, JSONField
from django.db import models
from django.contrib.auth.models import User
import services


class ParseTask(models.Model):
    name = models.CharField(max_length=200)
    login = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    service = models.CharField(max_length=2, choices=services.serviceEnums, default="AS")
    extra_data = HStoreField(default=list)
    result = JSONField(default=dict, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name
