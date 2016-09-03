from rest_framework.serializers import ModelSerializer
from blog.models import Post, Comment

class PostModelSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ('id','title','body')


class CommentModelSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id','message')

