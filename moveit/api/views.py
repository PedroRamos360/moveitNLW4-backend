from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .my_serializers import *
from django.core import serializers
from django.forms.models import model_to_dict
from json import dumps

class GetUser(generics.ListAPIView):
    serializer_class = UserSerializer
    def get(self, request, username=None, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                user = model_to_dict(User.objects.get(username=username))
                return Response(user, status=status.HTTP_200_OK)
            except:
                return Response({'Error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response("Error: Invalid data", status=status.HTTP_400_BAD_REQUEST)
    


class CreateUser(generics.ListAPIView):
    serializer_class = CreateUserSerializer
    queryset = ''
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            try: # se der certo é porque já existe um usuário com aquele nome
                user = model_to_dict(User.objects.get(username=data['username']))
                return Response({'Error': 'User already exists'}, status=status.HTTP_409_CONFLICT)
            except:
                users = User.objects.all()
                username = data['username']
                Id = users[len(users) -1].id + 1
                new_user = User(Id, username)
                new_user.save()
                return Response(model_to_dict(new_user), status=status.HTTP_200_OK)
        return Response({'Error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUser(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = ''
    def patch(self, request, format=None):
        try:
            data = request.data
            user = User.objects.get(username=data['username'])
            user.level = data['level']
            user.xp = data['xp']
            user.completed_challenges = data['completed_challenges']
            user.save(update_fields=['level', 'xp', 'completed_challenges'])
            return Response(model_to_dict(user), status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        


