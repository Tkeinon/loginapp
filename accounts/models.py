from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    organization_name = models.CharField('Organization', max_length=200)

    def __str__(self):
        return self.organization_name


class Users(models.Model):
    # model to extend existing user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
