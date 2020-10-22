from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
#######################################################3
class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}

        if len(post_data['title']) < 2:
            errors['title'] = "title must be at least 2 characters"

        if len(post_data['network']) < 3:
            errors['network'] = "network must be at least 2 characters"

        return errors
###############################################

class Show(models.Model):
    title = models.CharField(max_length=30)
    network = models.CharField(max_length=30)
    release = models.DateTimeField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager() # add this line!
