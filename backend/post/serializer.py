from rest_framework import serializers

from star.serializer import StarSerializerForPost
from post.models import Post, Comment, Likes, Dislikes
from user.serializer import UserSerializerForPost, UserProfile


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ('post_id', 'comment')


class CommentSerializerForPost(serializers.ModelSerializer):
    user = UserSerializerForPost(many=False)
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'comment', 'date', 'number_of_likes', 'number_of_dislikes', 'user')


class PostSerializer(serializers.ModelSerializer):
    star = StarSerializerForPost(many=False)
    user = UserSerializerForPost(many=False)
    users_comments = CommentSerializerForPost(many=True)

    class Meta:
        model = Post
        fields = ('id', 'locationY', 'locationX', 'title', 'photo',
                  'date', 'number_of_likes', 'number_of_dislikes', 'star', 'user', 'users_comments')


class LikesSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Likes
        fields = ('user_id', 'user_name')


class DislikesSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Dislikes
        fields = ('user_id', 'user_name')
