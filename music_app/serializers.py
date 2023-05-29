from rest_framework import serializers
from .models import User, MusicFile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class MusicFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicFile
        fields = ['title', 'file', 'visibility', 'allowed_emails', 'uploader']
        extra_kwargs = {'allowed_emails': {'required': False}}
