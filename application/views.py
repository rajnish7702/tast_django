from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def user_signip(request):
    serializer = UserSerializer(data=json.loads(request.body))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    data = json.loads(request.body)
    username = data.get('usernam')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if user is not  None:
        return Response("User Login Succesfull")
    return Response({"details":"Invalid User"},status=400)

