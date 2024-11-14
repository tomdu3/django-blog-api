from django.db import models
import uuid
from django.utils.text import slugify
from django.conf import settings


class Category(models.Model):
	name = models.CharField(unique=True, max_length=100)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return self.name

class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	category = models.ForeignKey('blogapp.Category', related_name='posts', on_delete=models.CASCADE)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
	title = models.CharField(unique=True, max_length=50)
	slug = models.SlugField(unique=True, max_length=50)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):

		return self.title

class Comment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
	post = models.ForeignKey('blogapp.Post', related_name='comments', on_delete=models.CASCADE)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

