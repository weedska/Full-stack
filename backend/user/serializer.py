from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from post.models import Post, Likes, Dislikes
from user.models import Followers, Profile, SavedPosts


class UserFollowerSerializer(serializers.ModelSerializer):
    follower_name = serializers.ReadOnlyField(source='followers.username')
    follower_id = serializers.ReadOnlyField(source='followers.id')

    class Meta:
        model = Followers
        fields = ('id', 'follower_name', 'follower_id')


class UserPostsSerializer(serializers.ModelSerializer):
    star_name = serializers.ReadOnlyField(source='api.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'star_name', 'date')


class AddUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
 #       extra_kwargs = {'username': {'write_only': True},
 #                       'password': {'write_only': True, 'required': True}}

 #   def create(self, validated_data):
 #       user = User.objects.create_user(**validated_data)
 #       Token.objects.create(user=user)
 #       return Token.objects.get(user=user)


class UserProfile(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'birth_date', 'location')


class LikedPostSerializer(serializers.ModelSerializer):
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Likes
        fields = ('post_id',)


class DislikedPostSerializer(serializers.ModelSerializer):
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Dislikes
        fields = ('post_id',)


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfile(many=False)
    user_followers = UserFollowerSerializer(many=True)
    user_posts = UserPostsSerializer(many=True)
    posts_liked = LikedPostSerializer(many=True)
    posts_disliked = DislikedPostSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'user_followers', 'user_posts', 'posts_liked', 'posts_disliked')


class UserProfileForPost(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('photo', 'number_of_posts', 'number_of_followers')


class UserSerializerForPost(serializers.ModelSerializer):
    profile = UserProfileForPost(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')


class SavedPostsSerializer(serializers.ModelSerializer):
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = SavedPosts
        fields = ('id', 'user', 'post_title')


class FollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Followers
        fields = ('user', "followers")
