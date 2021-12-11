from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def welcome(request):
    if request.method == 'GET':
        return JsonResponse({
            'response': 'welcome'
        })
        