from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=25)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	publication_date = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=50)
	body = models.TextField()
	category = models.ManyToManyField(Category)
	published = models.BooleanField(default=False)
	long_post = False

	def getComments(self):
		return self.comment_set.all()

	def numOfComments(self):
		return self.comment_set.all().count()
	
	def getCategoriesStr(self):
		return " ".join([c.name for c in self.category.all()])

	def __unicode__(self):
		return self.title


class Comment(models.Model):
	author = models.CharField(max_length=25)
	title = models.CharField(max_length=50)
	body = models.TextField()
	publication_date = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return self.author


class BlogRoll(models.Model):
	link = models.CharField(max_length=100)
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title






