from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticated(BasePermission):
	def has_permission(self, request, view):
		from .utils import decode_jwt
		user = decode_jwt(request.META.get('HTTP_AUTHORIZATION', None))
		if not user:
			return False
		request.user = user
		return True

class IsAuthenticatedOrReadOnly(BasePermission):
	def has_permission(self, request, view):
		if request.method in SAFE_METHODS:
			return True
		return IsAuthenticated().has_permission(request, view)
