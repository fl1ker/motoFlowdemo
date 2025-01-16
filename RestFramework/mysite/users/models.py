from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from mysite import settings
from auctions.models import Auction
from cars.models import Car


class ExtendedUser(AbstractUser):
    name = models.CharField(
        max_length=50,
        verbose_name=_("First Name"),
        help_text=_("User's first name"),
    )
    surname = models.CharField(
        max_length=50,
        verbose_name=_("Last Name"),
        help_text=_("User's last name"),
    )
    telephone = models.CharField(
        max_length=15,
        verbose_name=_("Telephone"),
        help_text=_("User's telephone number"),
        validators=[
            RegexValidator(
                regex=r"^\+?\d{9,15}$",
                message=_(
                    "Phone number must be in the format +123456789 and up to 15 digits."
                ),
            )
        ],
        null=True,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("Email"),
        help_text=_("User's email address"),
    )
    registration_date = models.DateTimeField(
        default=now,
        verbose_name=_("Registration Date"),
        help_text=_("Date when the user registered"),
    )
    last_login = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Last Login"),
        help_text=_("Last time the user logged in"),
    )

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["surname", "name"]


class FavouritesCars(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Odwołanie do modelu użytkownika
        on_delete=models.CASCADE,
        related_name="favourites",
        verbose_name=_("User"),
        help_text=_("The user who added the car to favourites"),
    )
    car = models.ForeignKey(
        Car,  # Odwołanie do modelu samochodu
        on_delete=models.CASCADE,
        related_name="favourited_by",
        verbose_name=_("Car"),
        help_text=_("The car that was added to favourites"),
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Date"),
        help_text=_("The date when the car was added to favourites"),
    )

    def __str__(self):
        return f"{self.user} liked {self.car}"

    class Meta:
        verbose_name = _("Favourite Car")
        verbose_name_plural = _("Favourite Cars")
        unique_together = ("user", "car")  # Unikalność relacji użytkownik-samochód
        ordering = ["-created_date"]


class CarRequest(models.Model):
    class RequestStatus(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", _("In Progress")
        COMPLETED = "COMPLETED", _("Completed")
        CANCELLED = "CANCELLED", _("Cancelled")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="car_requests",
        verbose_name=_("User"),
        help_text=_("The user who made the car request"),
    )
    brand = models.CharField(
        max_length=50,
        verbose_name=_("Brand"),
        help_text=_("Desired car brand"),
        null=True,
        blank=True,
    )
    model = models.CharField(
        max_length=50,
        verbose_name=_("Model"),
        help_text=_("Desired car model"),
        null=True,
        blank=True,
    )
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Budget"),
        help_text=_("Maximum budget for the car"),
    )
    status = models.CharField(
        max_length=15,
        choices=RequestStatus.choices,
        default=RequestStatus.IN_PROGRESS,
        verbose_name=_("Status"),
        help_text=_("Current status of the request"),
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created Date"),
        help_text=_("The date when the request was created"),
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated Date"),
        help_text=_("The date when the request was last updated"),
    )

    def __str__(self):
        return f"Request {self.pk} by {self.user} ({self.status})"

    class Meta:
        verbose_name = _("Car Request")
        verbose_name_plural = _("Car Requests")
        ordering = ["-created_date"]


class AuctionClicks(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="auction_clicks",
        verbose_name=_("User"),
        help_text=_("The user who clicked the auction"),
    )
    auction = models.ForeignKey(
        Auction,
        on_delete=models.CASCADE,
        related_name="user_clicks",
        verbose_name=_("Auction"),
        help_text=_("The auction that was clicked"),
    )
    click_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Click Count"),
        help_text=_("The number of times the user clicked the auction"),
    )
    last_click_date = models.DateTimeField(
        default=now,
        verbose_name=_("Last Click Date"),
        help_text=_("The date when the user last clicked the auction"),
    )

    def __str__(self):
        return f"{self.user} clicked {self.auction} {self.click_count} times"

    class Meta:
        verbose_name = _("Auction Click")
        verbose_name_plural = _("Auction Clicks")
        unique_together = (
            "user",
            "auction",
        )  # Użytkownik może mieć tylko jedną relację z daną aukcją
