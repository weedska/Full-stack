
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from star.views import StarViewSet, FollowersViewSet

router = routers.DefaultRouter()

router.register('stars', StarViewSet)
router.register('followers', FollowersViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
