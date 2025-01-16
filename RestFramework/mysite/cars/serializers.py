from rest_framework import serializers
from .models import Car, MetaCar, Performance, EngineInformation, Volume, Dimensions, Drivetrain



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class MetaCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaCar
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

class EngineInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineInformation
        fields = '__all__'

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'

class DimensionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimensions
        fields = '__all__'

class DrivetrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivetrain
        fields = '__all__'