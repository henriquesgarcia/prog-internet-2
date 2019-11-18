from rest_framework import serializers
from .models import Profile, Post, Comment
from django.contrib.auth.models import User


class PostSerializers(serializers.HyperlinkedModelSerializer):

	profile = serializers.SlugRelatedField(queryset = Profile.objects.all(),slug_field='name')
	owner = serializers.ReadOnlyField(source = 'owner.username')
	
	class Meta:
		model = Post
		fields = ('url','pk', 'title','body','profile', 'comments_quantity', 'owner')


class ProfilePostSerializers(serializers.HyperlinkedModelSerializer):

	posts = PostSerializers(many=True)

	class Meta:
		model = Profile
		fields = ('pk', 'username', 'name', 'email','posts')		


class ProfileSerializers(serializers.HyperlinkedModelSerializer):

	user = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field='username')
	
	class Meta:
		model = Profile
		fields = ('pk', 'username', 'name', 'email', 'user')	


class CommentSerializers(serializers.HyperlinkedModelSerializer):

	post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')

	class Meta:
		model = Comment
		fields = ('pk','post','name','email','body')