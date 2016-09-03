from rest_framework.viewsets import ModelViewSet
from blog.api.serializers import PostModelSerializer, CommentModelSerializer
from blog.models import Post, Comment

class PostModelViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostModelSerializer

class CommentModelViewSet(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentModelSerializer


