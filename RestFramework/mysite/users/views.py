from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import ExtendedUser, FavouritesCars, CarRequest, AuctionClicks
from users.serializers import ExtendedUserSerializer, FavouritesCarsSerializer, CarRequestSerializer, AuctionClicksSerializer


class ExtendedUserViewSet(viewsets.ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, )

class FavouritesCarsViewSet(viewsets.ModelViewSet):
    queryset = FavouritesCars.objects.all()
    serializer_class = FavouritesCarsSerializer

class CarRequestViewSet(viewsets.ModelViewSet):
    queryset = CarRequest.objects.all()
    serializer_class = CarRequestSerializer

class AuctionClicksViewSet(viewsets.ModelViewSet):
    queryset = AuctionClicks.objects.all()
    serializer_class = AuctionClicksSerializer


