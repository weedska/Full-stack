from rest_framework import serializers

from star.models import Star, StarPhoto, Followers
from post.models import Post


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarPhoto
        fields = ('photo',)


class FollowersSerializer(serializers.ModelSerializer):
    follower_name = serializers.ReadOnlyField(source='follower.username')
    # follower_photo

    class Meta:
        model = Followers
        fields = ('follower_id', 'follower_name',)


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'user_id', 'user', 'photo', 'date',)


class StarSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    photo = PhotoSerializer(many=False)
    followers = FollowersSerializer(many=True)
    posts = PostSerializer(many=True)

    class Meta:
        model = Star
        fields = ('id', 'user', 'first_name', 'last_name', 'sex', 'celebrity',
                  'country', 'photo', 'followers', 'posts')


class StarSerializerForPost(serializers.ModelSerializer):
    photo = PhotoSerializer(many=False)

    class Meta:
        model = Star
        fields = ('id', 'first_name', 'last_name', 'country', 'number_of_posts', 'number_of_followers', 'photo')


class FollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Followers
        fields = ('follower', 'star')
