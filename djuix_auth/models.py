from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomAuthManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('email field is required')

		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True')

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True')

		self.create_user(email, password, **extra_fields)


class CustomAuth (AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	is_staff =models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'email'
	objects = CustomAuthManager()

	def __str__(self):
		return self.email