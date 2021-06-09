from django.shortcuts import render
from django.http import JsonResponse #to return jSon responce
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'name': 'Sagar',
        'age': 25}
        return Response(data)
    
