from abc import ABC

from rest_framework import serializers
from .models import User


class getAllUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('userid', 'username', 'id',)


class userserializer(serializers.Serializer):
    userid = serializers.CharField(max_length=20)
    username = serializers.CharField(default=40)
    pword = serializers.CharField(max_length=20)
    id = serializers.IntegerField()

