from django.db import models


class repoDetails(models.Model):
    repository_name = models.CharField(max_length=100, null=False)
    repository_url = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)