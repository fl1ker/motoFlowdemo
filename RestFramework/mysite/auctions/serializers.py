from rest_framework import serializers
from .models import Auction, AuctionDocument, AuctionPhoto



class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'

class AuctionDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionDocument
        fields = '__all__'

class AuctionPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionPhoto
        fields = '__all__'

