from django.contrib import admin
from .models import Car, MetaCar, Performance, EngineInformation, Volume, Dimensions, Drivetrain


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "vin_number", "year_of_production", "type_of_fuel")
    search_fields = ("brand", "model", "vin_number")
    list_filter = ("year_of_production", "type_of_fuel", "gear_box")

@admin.register(MetaCar)
class MetaCarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "generation", "production_start_year", "production_end_year")
    search_fields = ("brand", "model", "generation")
    list_filter = ("production_start_year", "production_end_year", "body_type")

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("fuel_consumption_combined", "co2_emissions", "top_speed")
    search_fields = ("fuel_type",)
    list_filter = ("fuel_type", "ecological_standard")

@admin.register(EngineInformation)
class EngineInformationAdmin(admin.ModelAdmin):
    list_display = ("engine_power", "engine_layout", "cylinder_count", "fuel_injection_system")
    search_fields = ("engine_model_code",)
    list_filter = ("engine_layout", "fuel_injection_system")

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ("curb_weight_kg", "gross_vehicle_weight_kg", "trunk_capacity_liters", "fuel_tank_capacity_liters")

@admin.register(Dimensions)
class DimensionsAdmin(admin.ModelAdmin):
    list_display = ("length_mm", "width_mm", "height_mm", "wheelbase_mm")

@admin.register(Drivetrain)
class DrivetrainAdmin(admin.ModelAdmin):
    list_display = ("drivetrain", "transmission", "front_suspension", "rear_suspension")
    search_fields = ("drivetrain", "transmission")

