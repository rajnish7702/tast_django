from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','fist_name','last_name', 'email', 'password']
    def create(self, validated_data):
       user = User(username=validated_data['username'],
                   fist_name = validated_data['fist_name'],
                   last_name = validated_data['last_name'],
                   email=validated_data['email']
                )
       user.set_password(validated_data['password'])
       user.save()
       return user