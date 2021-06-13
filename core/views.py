from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers #to return jSon responce

from rest_framework.permissions import IsAuthenticated # allowany, you can allow anyone to use the api // Isauthenticated , authentication is required
from rest_framework.views import APIView
from rest_framework import mixins # mixins are the containers that provide the functionality like login req
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostView(mixins.ListModelMixin, mixins.CreateModelMixin,  generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    def get(self, request, *args, **kwargs):
        return self.list( request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #we dont need to call post method as CreateAPIView is already doing it, it only handles post method

    def get(self, request, *args, **kwargs):
        return self.list( request,*args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()





# class TestView(APIView):

#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)