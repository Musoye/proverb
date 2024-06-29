from django.shortcuts import render
from django.http import JsonResponse
from .models import Proverb
from .serializers import ProverbSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def proverb_list(request):

    if request.method == 'GET':
        proverbs = Proverb.objects.all()
        serializer = ProverbSerializer(proverbs, many=True)
        return JsonResponse({'proverbs': serializer.data})
    
    if request.method == 'POST':
        serializer = ProverbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def proverb_detail(request, id):
    try:
        proverb = Proverb.objects.get(pk=id)
    except Proverb.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        seriliazer = ProverbSerializer(proverb)
        return JsonResponse(seriliazer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProverbSerializer(proverb,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        proverb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
