from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CategorySerializer, CommentSerializer, PostSerializer
from .models import Category, Comment, Post


class Categoryviewset(viewsets.ModelViewSet):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = []
	search_fields = []
	pagination_class = None

class Postviewset(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	lookup_field = 'slug'
	queryset = Post.objects.all()
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['author', 'title', 'slug']
	search_fields = ['title', 'slug', 'text']

class Commentviewset(viewsets.ModelViewSet):
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['author', 'comment']
	search_fields = ['comment']

	def get_queryset(self):
		comments = Comment.objects.all()

		if self.request.query_params.get('post_slug', None):
			comments = Comment.objects.filter(post__slug__exact=self.request.query_params.get('post_slug', None))

		return comments

