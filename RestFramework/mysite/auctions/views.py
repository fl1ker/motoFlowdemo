from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from auctions.models import Auction, AuctionDocument, AuctionPhoto
from auctions.serializers import AuctionSerializer, AuctionDocumentSerializer, AuctionPhotoSerializer


class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class AuctionDocumentViewSet(viewsets.ModelViewSet):
    queryset = AuctionDocument.objects.all()
    serializer_class = AuctionDocumentSerializer

class AuctionPhotoViewSet(viewsets.ModelViewSet):
    queryset = AuctionPhoto.objects.all()
    serializer_class = AuctionPhotoSerializer

