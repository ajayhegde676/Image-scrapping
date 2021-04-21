from django.db import models


class user(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField(max_length=256)
    phone = models.CharField(max_length=256)

