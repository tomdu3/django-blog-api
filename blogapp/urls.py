from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
	Categoryviewset, Commentviewset, Postviewset,
)

router = DefaultRouter(trailing_slash=False)
router.register('category', Categoryviewset, basename='CategoryUrl')
router.register('post', Postviewset, basename='PostUrl')
router.register('comment', Commentviewset, basename='CommentUrl')

urlpatterns = [
	path('', include(router.urls)),
]