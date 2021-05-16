from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True, default='anonymous')
    level = models.IntegerField(null=False, default=1)
    xp = models.IntegerField(null=False, default=0)
    completed_challenges = models.IntegerField(null=False, default=0)


