from django.core.exceptions import ValidationError
from django.db import models

class ShowManager(models.Manager):
    def Show_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = "Show Title Must Be At Least 2 Characters"
        if len(post_data['network']) < 3:
            errors['network'] = "Network Must Be At Least 3 Characters"
        if 0 < len(post_data['description']) < 10:
            errors['description'] = "Description Must Be At Least 10 Characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()