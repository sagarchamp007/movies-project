# Create your models here.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    '''
    creating a manager for a custom user model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    '''
    def create_user(self, username, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not username:
            raise ValueError('Users Must Have an username')

        user = self.model(
            username=self.normalize_email(username),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.EmailField(
        verbose_name='username',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "users"
