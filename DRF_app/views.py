from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import postSerializer

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({"success": "set is successful"})

@api_view(['GET'])
def getallpost(request):
    posts=post.objects.all()
    serializer=postSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def createPost(request):
    data=request.data
    serializer=postSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success":"The post is successfuly created"}, status=201)
    else:
        return Response(serializer.errors, status=400)