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
#displaying the post 
@api_view(['GET'])
def getallpost(request):
    posts=post.objects.all()
    serializer=postSerializer(posts, many=True)
    return Response(serializer.data)
#creating the post
@api_view(['GET', 'POST'])
def createPost(request):
    data=request.data
    serializer=postSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success":"The post is successfuly created"}, status=201)
    else:
        return Response(serializer.errors, status=400)
    
#deliting the post 
@api_view(['DELETE'])
def delete(request):
    post_id=request.data.get('post_id')
    try:
        posts=post.objects.get(id=post_id)
        posts.delete()
        return Response({"success":"The post was successfull deleted"}, status=200)
    except post.DoesNotExist:
        return Response({"Error":"Post dose not exist"}, status=404)
    
#displaying one post    
@api_view(['GET'])
def get_post(request):
    pk=request.data.get('id')
    try:
        posts=post.objects.get(id=pk)
        serializer=postSerializer(posts)
        print(serializer)
        return Response(serializer.data)
    except post.DoesNotExist:
        return Response({"Error":"Post dose not exist"}, status=404)
    
#update the post
@api_view(['PUT'])
def updatePost(request):
    post_id=request.data.get('post_id')
    get_new_title=request.data.get('new_title')
    get_new_content=request.data.get('new_content')
    try:
        posts=post.objects.get(id=post_id)
        if get_new_title:
            posts.title=get_new_title
        if get_new_content:
            posts.content=get_new_content
        posts.save()
        return Response({"success":"post updated successfuly"})
    except post.DoesNotExist:
        return Response({"upda":"Post dose updated"})


    

