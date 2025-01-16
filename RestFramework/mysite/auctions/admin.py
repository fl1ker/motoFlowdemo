from django.contrib import admin
from .models import Auction, AuctionPhoto, AuctionDocument

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ("user", "car", "start_date", "end_date", "status", "type", "views_count")
    search_fields = ("user__username", "car__brand", "car__model")
    list_filter = ("status", "type", "start_date", "end_date")

@admin.register(AuctionPhoto)
class AuctionPhotoAdmin(admin.ModelAdmin):
    list_display = ("auction", "file", "uploaded_at")
    search_fields = ("auction__id",)

@admin.register(AuctionDocument)
class AuctionDocumentAdmin(admin.ModelAdmin):
    list_display = ("auction", "document", "uploaded_at")
    search_fields = ("auction__id",)
