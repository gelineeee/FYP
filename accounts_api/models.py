from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, address, password=None):
        """Create a new user profile"""
        if not address:
            raise ValueError('User must have an address')

        user = self.model(address=address)
        user.set_unusable_password()
        user.save(using=self._db)

        return user

    def create_superuser(self, address, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(address, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    address = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)  
    account_type = models.CharField(max_length=255, unique=False)
    phone = models.CharField(max_length=20, unique=True)
    member = models.BooleanField(default= False)
    points = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'address'

    def get_address(self):
        """Retrieve user address"""
        return self.address

    def get_name(self):
        """Retrieve user name"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.address
