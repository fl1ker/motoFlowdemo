from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    class FuelChoices(models.TextChoices):
        PETROL = "PETROL", _("Petrol")
        DIESEL = "DIESEL", _("Diesel")
        ELECTRIC = "ELECTRIC", _("Electric")
        HYBRID = "HYBRID", _("Hybrid")
        UNKNOWN = "UNKNOWN", _("Unknown")

    class GearBoxChoices(models.TextChoices):
        MANUAL = "MANUAL", _("Manual")
        AUTOMATIC = "AUTOMATIC", _("Automatic")
        UNKNOWN = "UNKNOWN", _("Unknown")

    class BodyTypeChoices(models.TextChoices):
        SEDAN = "SEDAN", _("Sedan")
        SUV = "SUV", _("SUV")
        HATCHBACK = "HATCHBACK", _("Hatchback")
        COUPE = "COUPE", _("Coupe")
        CONVERTIBLE = "CONVERTIBLE", _("Convertible")
        OTHER = "OTHER", _("Other")
        UNKNOWN = "UNKNOWN", _("Unknown")

    brand = models.CharField(
        max_length=50, verbose_name=_("Brand"), help_text=_("Brand of the car")
    )
    model = models.CharField(
        max_length=50, verbose_name=_("Model"), help_text=_("Model of the car")
    )
    registration_number = models.CharField(
        max_length=15,
        verbose_name=_("Registration Number"),
        help_text=_("Registration number of the car"),
    )
    vin_number = models.CharField(
        max_length=17,
        unique=True,
        db_index=True,
        verbose_name=_("VIN"),
        help_text=_("Unique Vehicle Identification Number"),
    )
    date_of_first_registration = models.DateField(
        verbose_name=_("First Registration Date"),
        help_text=_("The date when the car was first registered"),
    )
    body_type = models.CharField(
        max_length=50,
        choices=BodyTypeChoices,
        default=BodyTypeChoices.UNKNOWN,
        verbose_name=_("Body Type"),
        help_text=_("Type of the car body (e.g., sedan, SUV)"),
    )
    year_of_production = models.PositiveIntegerField(
        verbose_name=_("Year of Production"),
        help_text=_("The year the car was produced"),
    )
    engine_capacity = models.PositiveIntegerField(
        verbose_name=_("Engine Capacity (ccm)"), help_text=_("Engine capacity in ccm)")
    )
    engine_power = models.PositiveIntegerField(
        verbose_name=_("Engine Power (HP)"), help_text=_("Engine power in horsepower")
    )
    gear_box = models.CharField(
        max_length=10,
        choices=GearBoxChoices,
        default=BodyTypeChoices.UNKNOWN,
        verbose_name=_("Gear Box"),
        help_text=_("Type of gear box (manual or automatic)"),
    )
    type_of_fuel = models.CharField(
        max_length=10,
        choices=FuelChoices,
        default=BodyTypeChoices.UNKNOWN,
        verbose_name=_("Fuel Type"),
        help_text=_("Type of fuel used by the car"),
    )
    mileage = models.PositiveIntegerField(
        verbose_name=_("Mileage (km)"),
        help_text=_("Total mileage of the car in kilometers"),
    )
    damage_condition = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Damage Condition"),
        help_text=_("Details about the car's damage condition, if any"),
    )
    meta_car = models.ForeignKey(
        "MetaCar",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="related_cars",
        verbose_name=_("Meta Car"),
        help_text=_("Detailed information from the database"),
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year_of_production})"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ["brand", "model"]


class MetaCar(models.Model):
    brand = models.CharField(max_length=50, verbose_name=_("Brand"))
    model = models.CharField(max_length=50, verbose_name=_("Model"))
    generation = models.CharField(max_length=50, verbose_name=_("Generation"))
    production_start_year = models.PositiveIntegerField(
        verbose_name=_("Production Start Year")
    )
    production_end_year = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_("Production End Year")
    )
    body_type = models.CharField(max_length=50, verbose_name=_("Body Type"))
    seating_capacity = models.PositiveIntegerField(verbose_name=_("Seating Capacity"))
    door_count = models.PositiveIntegerField(verbose_name=_("Door Count"))

    # Relacje do szczegółowych modeli
    performance = models.OneToOneField(
        "Performance",
        on_delete=models.CASCADE,
        related_name="meta_car",
        verbose_name=_("Performance"),
    )
    engine_information = models.OneToOneField(
        "EngineInformation",
        on_delete=models.CASCADE,
        related_name="meta_car",
        verbose_name=_("Engine Information"),
    )
    volume = models.OneToOneField(
        "Volume",
        on_delete=models.CASCADE,
        related_name="meta_car",
        verbose_name=_("Volume"),
    )
    dimensions = models.OneToOneField(
        "Dimensions",
        on_delete=models.CASCADE,
        related_name="meta_car",
        verbose_name=_("Dimensions"),
    )
    drivetrain = models.OneToOneField(
        "Drivetrain",
        on_delete=models.CASCADE,
        related_name="meta_car",
        verbose_name=_("Drivetrain"),
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.generation})"

    class Meta:
        verbose_name = _("Meta Car")
        verbose_name_plural = _("Meta Cars")
        ordering = ["brand", "model", "generation"]


class Performance(models.Model):
    fuel_consumption_city = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Fuel Consumption (City)")
    )
    fuel_consumption_highway = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Fuel Consumption (Highway)")
    )
    fuel_consumption_combined = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Fuel Consumption (Combined)")
    )
    co2_emissions = models.PositiveIntegerField(verbose_name=_("CO2 Emissions (g/km)"))
    fuel_type = models.CharField(max_length=50, verbose_name=_("Fuel Type"))
    acceleration_0_100_kmh = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name=_("Acceleration (0-100 km/h)")
    )
    top_speed = models.PositiveIntegerField(verbose_name=_("Top Speed (km/h)"))
    ecological_standard = models.CharField(
        max_length=50, verbose_name=_("Ecological Standard")
    )
    weight_to_power_ratio = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Weight-to-Power Ratio")
    )
    torque_to_weight_ratio = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Torque-to-Weight Ratio")
    )


class EngineInformation(models.Model):
    engine_power = models.PositiveIntegerField(verbose_name=_("Engine Power (HP)"))
    torque = models.PositiveIntegerField(verbose_name=_("Torque (Nm)"))
    engine_layout = models.CharField(max_length=50, verbose_name=_("Engine Layout"))
    engine_model_code = models.CharField(
        max_length=50, verbose_name=_("Engine Model Code")
    )
    engine_capacity_cc = models.PositiveIntegerField(
        verbose_name=_("Engine Capacity (ccm)")
    )
    cylinder_count = models.PositiveIntegerField(verbose_name=_("Cylinder Count"))
    cylinder_configuration = models.CharField(
        max_length=50, verbose_name=_("Cylinder Configuration")
    )
    bore_mm = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Bore (mm)")
    )
    stroke_mm = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Stroke (mm)")
    )
    compression_ratio = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name=_("Compression Ratio")
    )
    valves_per_cylinder = models.PositiveIntegerField(
        verbose_name=_("Valves per Cylinder")
    )
    fuel_injection_system = models.CharField(
        max_length=100, verbose_name=_("Fuel Injection System")
    )
    turbocharging = models.BooleanField(default=False, verbose_name=_("Turbocharging"))
    engine_oil_capacity_liters = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name=_("Engine Oil Capacity (Liters)")
    )
    coolant_capacity_liters = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name=_("Coolant Capacity (Liters)")
    )


class Volume(models.Model):
    curb_weight_kg = models.PositiveIntegerField(verbose_name=_("Curb Weight (kg)"))
    gross_vehicle_weight_kg = models.PositiveIntegerField(
        verbose_name=_("Gross Vehicle Weight (kg)")
    )
    max_load_kg = models.PositiveIntegerField(verbose_name=_("Max Load (kg)"))
    trunk_capacity_liters = models.PositiveIntegerField(
        verbose_name=_("Trunk Capacity (liters)")
    )
    fuel_tank_capacity_liters = models.PositiveIntegerField(
        verbose_name=_("Fuel Tank Capacity (liters)")
    )
    max_towed_weight_braked_kg = models.PositiveIntegerField(
        verbose_name=_("Max Towed Weight Braked (kg)")
    )
    max_towed_weight_unbraked_kg = models.PositiveIntegerField(
        verbose_name=_("Max Towed Weight Unbraked (kg)")
    )
    tow_hook_max_vertical_load_kg = models.PositiveIntegerField(
        verbose_name=_("Tow Hook Max Vertical Load (kg)")
    )


class Dimensions(models.Model):
    length_mm = models.PositiveIntegerField(verbose_name=_("Length (mm)"))
    width_mm = models.PositiveIntegerField(verbose_name=_("Width (mm)"))
    width_with_mirrors_mm = models.PositiveIntegerField(
        verbose_name=_("Width with Mirrors (mm)")
    )
    height_mm = models.PositiveIntegerField(verbose_name=_("Height (mm)"))
    wheelbase_mm = models.PositiveIntegerField(verbose_name=_("Wheelbase (mm)"))
    ground_clearance_mm = models.PositiveIntegerField(
        verbose_name=_("Ground Clearance (mm)")
    )
    aerodynamic_drag_coefficient = models.DecimalField(
        max_digits=4, decimal_places=3, verbose_name=_("Aerodynamic Drag Coefficient")
    )
    minimum_turning_diameter_m = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name=_("Minimum Turning Diameter (m)")
    )


class Drivetrain(models.Model):
    drivetrain = models.CharField(max_length=50, verbose_name=_("Drivetrain"))
    transmission = models.CharField(max_length=50, verbose_name=_("Transmission"))
    front_suspension = models.CharField(
        max_length=100, verbose_name=_("Front Suspension")
    )
    rear_suspension = models.CharField(
        max_length=100, verbose_name=_("Rear Suspension")
    )
    front_brakes = models.CharField(max_length=50, verbose_name=_("Front Brakes"))
    rear_brakes = models.CharField(max_length=50, verbose_name=_("Rear Brakes"))
    steering_type = models.CharField(max_length=50, verbose_name=_("Steering Type"))
    steering_assist = models.CharField(max_length=50, verbose_name=_("Steering Assist"))
    tire_size = models.CharField(max_length=50, verbose_name=_("Tire Size"))
    wheel_size = models.CharField(max_length=50, verbose_name=_("Wheel Size"))
