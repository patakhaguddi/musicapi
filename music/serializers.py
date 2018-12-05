from django.contrib.auth.models import User
from rest_framework import serializers
from music.models import Songs


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("id", "title", "album", "artist", "bio", "release_time")

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.artist = validated_data.get("artist", instance.artist)
        instance.album = validated_data.get("album", instance.album)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.release_time = validated_data.get("release_time", instance.release_time)
        instance.save()
        return instance

class TokenSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

