from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def welcome(request):
    if request.method == 'GET':
        return render(request, "index/welcome.html")
        