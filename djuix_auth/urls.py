from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, RegisterView, RefreshView, ActiveUserView

router = DefaultRouter(trailing_slash=False)
router.register('login', LoginView, basename='login')
router.register('register', RegisterView, basename='register')
router.register('refresh', RefreshView, basename='refresh')
router.register('active', ActiveUserView, basename='active')

urlpatterns = [
	path('', include(router.urls)),
]