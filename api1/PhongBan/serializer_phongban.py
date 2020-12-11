from rest_framework import serializers
from api1.PhongBan.model_phongban import User1


class getAllUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User1
        # fields = '__all__'
        fields = ('userid', 'username', 'id',)


class userserializer(serializers.Serializer):
    userid = serializers.CharField(max_length=20)
    username = serializers.CharField(default=40)
    pword = serializers.CharField(max_length=20)
    id = serializers.IntegerField()