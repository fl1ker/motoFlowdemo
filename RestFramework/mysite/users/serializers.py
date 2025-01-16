from rest_framework import serializers
from .models import ExtendedUser, FavouritesCars, CarRequest, AuctionClicks



class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = '__all__'

class FavouritesCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritesCars
        fields = '__all__'

class CarRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRequest
        fields = '__all__'

class AuctionClicksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionClicks
        fields = '__all__'