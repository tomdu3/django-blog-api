from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CustomAuth
from .serializers import LoginSerializer, RefreshSerializer, CustomAuthSerializer
from .utils import get_access_token, get_refresh_token, verify_token
from .methods import IsAuthenticated


class LoginView(ModelViewSet):
	queryset = CustomAuth.objects.all()
	serializer_class = LoginSerializer
	permission_classes = []
	http_method_names = ['post']

	def create(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		user = authenticate(username=serializer.validated_data['email'], password=serializer.validated_data['password'])
		if not user:
			return Response({'error': 'Invalid credentials'}, status=400)
		access_token = get_access_token({'user_id': user.id})
		refresh_token = get_refresh_token()
		return Response({'access': access_token, 'refresh': refresh_token})

class RegisterView(ModelViewSet):
	queryset = CustomAuth.objects.all()
	serializer_class = CustomAuthSerializer
	permission_classes = []
	http_method_names = ['post']

	def create(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = CustomAuth.objects.create_user(**serializer.validated_data)
		return Response(self.get_serializer(user).data)

class RefreshView(ModelViewSet):
	queryset = CustomAuth.objects.all()
	serializer_class = RefreshSerializer
	permission_classes = []
	http_method_names = ['post']

	def create(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		refresh = serializer.validated_data['refresh']
		user = verify_token(refresh)

		if not user:
			return Response({'error': 'Invalid refresh token'}, status=400)

		access_token = get_access_token(user)
		return Response({'access': access_token})

class ActiveUserView(ModelViewSet):
	queryset = CustomAuth.objects.all()
	serializer_class = CustomAuthSerializer
	http_method_names = ['get']
	permission_classes = [IsAuthenticated]

	def list(self, request):
		return Response(self.get_serializer(request.user).data)
