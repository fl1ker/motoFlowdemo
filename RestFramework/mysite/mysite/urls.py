"""
URL configuration for MotoFlow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import *
from cars.views import *
from blogs.views import *
from auctions.views import *


router = routers.SimpleRouter()
router.register(r'users',  ExtendedUserViewSet)
router.register(r'favourite', FavouritesCarsViewSet)
router.register(r'carrequest', CarRequestViewSet)
router.register(r'auctionclicks', AuctionClicksViewSet)

router.register(r'cars', CarViewSet)
router.register(r'metacar', MetaCarViewSet)
router.register(r'perfomance', PerformanceViewSet)
router.register(r'engine', EngineInformationViewSet)
router.register(r'volume', VolumeViewSet)
router.register(r'dimensions', DimensionsViewSet)
router.register(r'drivetrain', DrivetrainViewSet)

router.register(r'blogcontent', BlogContentViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'blogimage', BlogImageViewSet)

router.register(r'auctions', AuctionViewSet)
router.register(r'auctiondocument', AuctionDocumentViewSet)
router.register(r'auctionphoto', AuctionPhotoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    path("api/motoflow-auth/", include('rest_framework.urls')),

    path("api/auth/", include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),


    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name = 'token_verify'),
]
