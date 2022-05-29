from django.contrib import admin

# Register your models here.
from star.models import Star, Followers, StarPhoto


admin.site.register(Star)
admin.site.register(StarPhoto)
admin.site.register(Followers)
