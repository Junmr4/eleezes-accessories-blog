from rest_framework.serializers import ModelSerializer
from blog.models import Post, Comment

class PostModelSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'


class CommentModelSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
