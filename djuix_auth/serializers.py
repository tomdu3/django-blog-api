from rest_framework import serializers
from .models import CustomAuth

class CustomAuthSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomAuth
		fields = '__all__'
		extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()

class RefreshSerializer(serializers.Serializer):
	refresh = serializers.CharField()