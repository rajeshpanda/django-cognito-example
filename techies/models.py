import uuid
from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager as _UserManager
from django.contrib.auth.models import Group


class CogUserManager(_UserManager):
    def get_or_create_for_cognito(self, payload):
        cognito_id = payload['sub']
        group = payload['cognito:groups']
        try:
            user = self.get(cognito_id=cognito_id)   
            new_group, created = Group.objects.get_or_create(name=group[0])
            user.groups.set([new_group])
            return user
        except self.model.DoesNotExist:
            pass

        try:
            user = self.create(
                cognito_id=cognito_id,
                email=payload['email'],
                is_active=True)
            new_group, created = Group.objects.get_or_create(name=group[0])
            user.groups.set([new_group])
            return user
        except IntegrityError:
            user = self.get(cognito_id=cognito_id)
            new_group, created = Group.objects.get_or_create(name=group[0])
            user.groups.set([new_group])
            return user
        return user


class CogUser(AbstractBaseUser, PermissionsMixin):
    cognito_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=150, null=False,
                             unique=True, default="x")
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'cognito_id'
    objects = CogUserManager()


class talent(models.Model):
    id: models.UUIDField(primary_key=True)
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.firstName
