from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs  = {"password": {"write_only": True}} # password is not returned in the response
        
    def create(self, validated_data): # override the create method to hash the password
        user  = User.objects.create_user(**validated_data) # **validated_data unpacks the dictionary
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}} # author is not returned in the response

