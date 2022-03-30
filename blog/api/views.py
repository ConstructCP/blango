from rest_framework import generics

from ..models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blango_auth.models import User


class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]


class UserDetail(generics.RetrieveAPIView):
  lookup_field = 'email'
  queryset = User.objects.all()
  serializer_class = UserSerializer
