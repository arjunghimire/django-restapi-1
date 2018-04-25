#from django.contrib.auth.models import Blog
from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'body')
