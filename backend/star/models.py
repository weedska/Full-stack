from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class Star(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='stars_created')
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, default='')

    class Sex(models.TextChoices):
        Male = 'MALE'
        Female = 'FEMALE'

    sex = models.CharField(max_length=6, choices=Sex.choices)

    country = CountryField(null=True)

    class CelebType(models.TextChoices):
        People = 'People'
        Model = 'Model'
        Actor_Actress = 'Actor-Actress'
        Artist = 'Artist'
        Athlete = 'Athlete'
        Businessman = 'Businessman'
        Politician = 'Politician'
        Scientist = 'Scientist'

    celebrity = models.CharField(max_length=32, choices=CelebType.choices)

    def number_of_posts(self):
        posts = self.posts
        return len(posts.filter())

    def number_of_followers(self):
        followers = Followers.objects.filter(star=self)
        return len(followers.filter())

    def __str__(self):
        return self.first_name


class StarPhoto(models.Model):

    def directory(instance, star_id):
        return "photos/cover/star_{0}/{1}".format(instance.star.id, star_id)

    photo = models.ImageField(upload_to=directory)
    star = models.OneToOneField(Star, on_delete=models.CASCADE, related_name='photo')

    def __str__(instance):
        return '{0}s photo'.format(instance.star.first_name)


class Followers (models.Model):
    follower = models.ForeignKey(User, default=0, on_delete=models.CASCADE, related_name='stars')
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return '{0} followed {1}'.format(self.follower.username, self.star)



