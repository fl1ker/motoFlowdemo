from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from cars.models import Car, MetaCar, Performance, EngineInformation, Volume, Dimensions, Drivetrain
from cars.serializers import CarSerializer, MetaCarSerializer, PerformanceSerializer, EngineInformationSerializer, VolumeSerializer, DimensionsSerializer, DrivetrainSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class MetaCarViewSet(viewsets.ModelViewSet):
    queryset = MetaCar.objects.all()
    serializer_class = MetaCarSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

class EngineInformationViewSet(viewsets.ModelViewSet):
    queryset = EngineInformation.objects.all()
    serializer_class = EngineInformationSerializer

class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

class DimensionsViewSet(viewsets.ModelViewSet):
    queryset = Dimensions.objects.all()
    serializer_class = DimensionsSerializer

class DrivetrainViewSet(viewsets.ModelViewSet):
    queryset = Drivetrain.objects.all()
    serializer_class = DrivetrainSerializer


