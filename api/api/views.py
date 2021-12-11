from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        return JsonResponse({
            'response': 'hi'
        })