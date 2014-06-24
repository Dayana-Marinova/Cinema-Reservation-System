from django.db import models


class SignUp(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username
