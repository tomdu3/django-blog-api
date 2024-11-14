from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
	category = serializers.CharField(read_only=True)
	category_id = serializers.CharField(write_only=True)
	author = serializers.CharField(read_only=True)
	author_id = serializers.CharField(write_only=True)
	class Meta:
		model = Post
		fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
	author = serializers.CharField(read_only=True)
	author_id = serializers.CharField(write_only=True)
	post = serializers.CharField(read_only=True)
	post_id = serializers.CharField(write_only=True)
	class Meta:
		model = Comment
		fields = '__all__'

