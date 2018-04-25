from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=30)
	body = models.CharField(max_length=1000)
	