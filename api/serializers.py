#seralizer transfers the models into json response
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id','code','host','guests_can_pause','votes_to_skip','created_at') #id is for primary key 


class CreateRoomSerializer(serializers.ModelSerializer): #whenever dealing with request use seraillizers
    class Meta:
        model=Room
        fields=('guests_can_pause','votes_to_skip')

class UpdateRoomSerializer(serializers.ModelSerializer): #whenever dealing with request use seraillizers
    code=serializers.CharField(validators=[])
    
    class Meta:
        model=Room
        fields=('guests_can_pause','votes_to_skip','code')