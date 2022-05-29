
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from post.models import Post


class Profile(models.Model):

    def directory(instance, user):
        return "photos/cover/user_{0}/{1}".format(instance.user.id, user)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fb_id = models.CharField(max_length=64, blank=True)
    photo = models.ImageField(upload_to=directory, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    # Without choosing a country there is an error, need to be set default country
    location = CountryField(null=True, blank=True, default='LT')

    birth_date = models.DateField(null=True, blank=True)

    def number_of_posts(self):
        return len(self.user.user_posts.filter())

    def number_of_followers(self):
        return len(self.user.user_followers.filter())

    def __str__(self):
        return '{0} s profile'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Followers(models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE, related_name='user_followers')
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_user')

    def __str__(self):
        return '{0} followed {1}'.format(self.followers.username, self.user.username)


class SavedPosts(models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE, related_name='user_saved_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saved_post')

    def __str__(self):
        return '{0} saved {1}'.format(self.user.username, self.post.title)
