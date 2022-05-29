
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from post.views import PostViewSet, CommentViewSet



router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]