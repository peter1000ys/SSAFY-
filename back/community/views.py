from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewListSerializer, CommentSerializer, ReviewSerializer, ReviewDetailSerializer
from .models import Review,Comment
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework import status

from django.http import HttpResponse

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list(request):
  if request.method == 'GET':
    print('get')
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
  if request.method == 'GET':
    review = Review.objects.get(pk=review_pk)
    serializer = ReviewDetailSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
def review_like(request):
  pass

@api_view(['POST'])
def review_hate(request):
  pass

@api_view(['GET', 'POST'])
def review_comment(request):
  pass

@api_view(['POST'])
def review_comment_like(request):
  pass

@api_view(['POST'])
def review_comment_hate(request):
  pass