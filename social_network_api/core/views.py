from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions, mixins, generics
from .models import Profile, Post, Comment
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.throttling import ScopedRateThrottle
from .serializers import ProfileSerializers, PostSerializers,ProfilePostSerializers, CommentSerializers

# Create your views here.
class Profiles(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

	queryset = Profile.objects.all()
	serializer_class = ProfileSerializers

	def get_permissions(self):
		return [permissions.IsAuthenticated(),]


class Posts(ModelViewSet):

	queryset = Post.objects.all()
	serializer_class = PostSerializers
	
	def get_permissions(self):
		return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]

	def get_queryset(self):

		try:
			return Post.objects.filter(profile = self.kwargs['user_pk'])
		except KeyError:
			return Post.objects.all()


class ProfilePosts(ModelViewSet):

	queryset = Profile.objects.all()
	serializer_class = ProfilePostSerializers


class Comments(ModelViewSet):

	queryset = Comment.objects.all()
	serializer_class = CommentSerializers

	def get_permissions(self):
		return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]

	def get_queryset(self):
		return Comment.objects.filter(post=self.kwargs['post_pk'])


class ApiRoot(generics.GenericAPIView):

	name = 'api-root'

	def get(self, request, *args, **kwargs):
		return Response({
			'Profile': reverse('users', request  = request),
			'Posts': reverse('posts', request  = request),
			'Comments': reverse('comments', request  = request),
			'Users-post': reverse('users-posts', request  = request)
			})


class CustomAuthToken(ObtainAuthToken):

	throttle_scope = 'token_request'
	throttle_classes = (ScopedRateThrottle,)

	def post(self, request, *args, **kwargs):

		serializer = self.serializer_class(data=request.data, context={'request': request})

		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)

		return Response({'token': token.key, 'user_id': user.pk, 'name': user.first_name})


		