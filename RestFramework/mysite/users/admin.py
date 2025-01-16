from django.contrib import admin
from .models import ExtendedUser, CarRequest, AuctionClicks, FavouritesCars

@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "name", "surname", "registration_date")
    search_fields = ("username", "email", "name", "surname")
    list_filter = ("registration_date",)

@admin.register(CarRequest)
class CarRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "brand", "model", "budget", "status", "created_date")
    search_fields = ("brand", "model", "user__username")
    list_filter = ("status", "created_date")

@admin.register(AuctionClicks)
class AuctionClicksAdmin(admin.ModelAdmin):
    list_display = ("user", "auction", "click_count", "last_click_date")
    search_fields = ("user__username", "auction__id")

@admin.register(FavouritesCars)
class FavouritesCarsAdmin(admin.ModelAdmin):
    list_display = ("user", "car", "created_date")
    search_fields = ("user__username", "car__id")
