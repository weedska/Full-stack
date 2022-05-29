
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from user.views import AddUserViewSet, UserViewSet, SavedPostsViewSet, FollowersViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('add', AddUserViewSet)
router.register('saved_posts', SavedPostsViewSet)
router.register('followers', FollowersViewSet)


urlpatterns = [
    path('', include(router.urls)),
]