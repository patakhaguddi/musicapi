# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import authentication, permissions, generics
# Create your views here.
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import status

from music.serializers import RegisterSerializer, LoginSerializer
from .models import Songs
from .serializers import SongsSerializer, TokenSerializer, UserSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from .decorators import validate_request_data

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class ListSongsView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_song = Songs.objects.create(
            title=request.data["title"],
            artist=request.data["artist"],
            # ,
            album=request.data["album"],
            bio=request.data["bio"]
            # release_time=request.data["release_time"]
        )
        return Response(
            data=SongsSerializer(a_song).data,
            status=status.HTTP_201_CREATED
        )


class SongsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongsSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            return Response(SongsSerializer(a_song).data)
        except Songs.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    # @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            serializer = SongsSerializer()
            updated_song = serializer.update(a_song, request.data)
            return Response(SongsSerializer(updated_song).data)
        except Songs.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format()
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            a_song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Songs.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format()
                },
                status=status.HTTP_404_NOT_FOUND
            )

class LoginView(generics.CreateAPIView):

    serializer_class = LoginSerializer


    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            serializer = TokenSerializer(data={

                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )}
                )
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAITHORIZED)

class RegisterUsersView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")

        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"

                },
                status=status.HTTP_400_BAD_REQUEST

            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=UserSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )








