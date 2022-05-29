from django.db import models

from star.models import Star
from django.contrib.auth.models import User


class Post (models.Model):
    def directory(instance, star):
        return "photos/star_{0}/{1}".format(instance.star.id, star)

    title = models.CharField(max_length=120, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField(upload_to=directory)
    date = models.DateTimeField()
    locationY = models.FloatField()
    locationX = models.FloatField()
    n18 = models.BooleanField(default=False)

    def number_of_likes(self):
        return len(self.likes.filter())

    def number_of_dislikes(self):
        return len(self.dislikes.filter())



    def __str__(self):
        return '{0} - {1}'.format(self.star, self.date)


class Likes (models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE, related_name='posts_liked')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return '{0} liked {1}'.format(self.user.username, self.post.title)


class Dislikes (models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE, related_name='posts_disliked')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislikes')

    def __str__(self):
        return '{0} disliked {1}'.format(self.user.username, self.post.title)


class Comment (models.Model):
    comment = models.TextField(max_length=460)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='users_comments')
    date = models.DateTimeField()

    def number_of_likes(self):
        return len(self.users_liked.filter())

    def number_of_dislikes(self):
        return len(self.users_disliked.filter())

    def __str__(self):
        return '{0}: {1} - {2}'.format(self.user.username, self.comment, self.post.star.first_name)


class CommentLikes (models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE, related_name='comment_liked')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='users_liked')

    def __str__(self):
        return '{0} liked "{1}" comment'.format(self.user.username, self.comment.comment)


class CommentDislikes (models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE, related_name='comments_disliked')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='users_disliked')

    def __str__(self):
        return '{0} disliked "{1}" comment'.format(self.user.username, self.comment.comment)
