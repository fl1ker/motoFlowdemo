from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from blogs.models import BlogContent, Blog, BlogImage
from blogs.serializers import BlogContentSerializer, BlogSerializer, BlogImageSerializer


class BlogContentViewSet(viewsets.ModelViewSet):
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogImageViewSet(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer

