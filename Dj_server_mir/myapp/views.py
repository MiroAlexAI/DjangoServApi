from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
import requests

def welcome(request):
    api_url = 'http://127.0.0.1:8000/api/users/'
    response = requests.get(api_url)

    if response.status_code == 200:
        users = response.json()
        return render(request, 'welcome.html', {'users': users})
    else:
        error_message = f"Failed to fetch users. Status code: {response.status_code}"
        return render(request, 'welcome.html', {'error_message': error_message})

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CreateUserView(APIView):
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)