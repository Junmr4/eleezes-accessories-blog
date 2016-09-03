from rest_framework import routers
from blog.api.views import PostModelViewSet, CommentModelViewSet

routers = routers.DefaultRouter()	
routers.register('Post', PostModelViewSet)
routers.register('Comment', CommentModelViewSet)
urlpatterns = routers.urls