from django.db import models
# Create your models here.

class Profile(models.Model):

	user = models.ForeignKey('auth.User', related_name='user_profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=70)
	username = models.CharField(max_length=45)
	email = models.CharField(max_length=70)
	address = models.OneToOneField('Address',related_name='profile' ,null=True ,on_delete=models.SET_NULL)	


class Address(models.Model):

	street = models.CharField(max_length=100)
	suite = models.CharField(max_length=45)
	city = models.CharField(max_length=45)
	zipcode = models.CharField(max_length=15)


class Post(models.Model):

	title = models.CharField(max_length=45)
	body = models.CharField(max_length=140)
	profile = models.ForeignKey('Profile', related_name='posts', on_delete=models.CASCADE)
	owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

	@property
	def comments_quantity(self):
		return self.comments.all().count()


class Comment(models.Model):

	name = models.CharField(max_length=45)
	email = models.CharField(max_length=70)
	body = models.CharField(max_length=140)
	post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
