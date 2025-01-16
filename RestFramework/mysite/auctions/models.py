from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from cars.models import Car
from media.models import Image


class Auction(models.Model):
    class AuctionStatus(models.TextChoices):
        ACTIVE = "ACTIVE", _("Active")
        INACTIVE = "INACTIVE", _("Inactive")
        COMPLETED = "COMPLETED", _("Completed")
        CANCELLED = "CANCELLED", _("Cancelled")

    class AuctionType(models.TextChoices):
        PRIVATE = "PRIVATE", _("Private")
        BUSINESS = "BUSINESS", _("Business")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="auctions",
        verbose_name=_("User"),
        help_text=_("The user who created the auction"),
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="auctions",
        verbose_name=_("Car"),
        help_text=_("The car being auctioned"),
    )
    start_date = models.DateTimeField(
        default=now,
        verbose_name=_("Start Date"),
        help_text=_("The date when the auction starts"),
    )
    end_date = models.DateTimeField(
        verbose_name=_("End Date"), help_text=_("The date when the auction ends")
    )
    likes = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Likes"),
        help_text=_("Number of likes received by the auction"),
    )
    dislikes = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Dislikes"),
        help_text=_("Number of dislikes received by the auction"),
    )
    clicks = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Clicks"),
        help_text=_("Number of clicks on the auction"),
    )
    localization = models.CharField(
        max_length=100,
        verbose_name=_("Localization"),
        help_text=_("Location of the car being sold"),
    )
    status = models.CharField(
        max_length=15,
        choices=AuctionStatus.choices,
        default=AuctionStatus.ACTIVE,
        verbose_name=_("Status"),
        help_text=_("Current status of the auction"),
    )
    type = models.CharField(
        max_length=15,
        choices=AuctionType.choices,
        default=AuctionType.PRIVATE,
        verbose_name=_("Type"),
        help_text=_("Type of the auction: private or business"),
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Views Count"),
        help_text=_("Number of views the auction has received"),
    )

    def __str__(self):
        return f"Auction {self.pk} for {self.car} by {self.user}"

    class Meta:
        verbose_name = _("Auction")
        verbose_name_plural = _("Auctions")
        ordering = ["-start_date"]


class AuctionDocument(models.Model):
    auction = models.ForeignKey(
        Auction,
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name=_("Auction"),
        help_text=_("The auction this document belongs to"),
    )
    document = models.FileField(
        upload_to="auction_documents/",
        verbose_name=_("Document"),
        help_text=_("A document related to the auction, e.g., car history"),
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Uploaded At"),
        help_text=_("The date and time when the document was uploaded"),
    )

    def __str__(self):
        return f"Document for Auction {self.auction.id}"

    class Meta:
        verbose_name = _("Auction Document")
        verbose_name_plural = _("Auction Documents")
        ordering = ["-uploaded_at"]


class AuctionPhoto(Image):
    auction = models.ForeignKey(
        Auction, on_delete=models.CASCADE, related_name="photos"
    )
