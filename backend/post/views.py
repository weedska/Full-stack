
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response

from star.models import Star
from post.models import Post, Comment, Likes, Dislikes, CommentLikes, CommentDislikes
from post.serializer import PostSerializer, CommentSerializer, LikesSerializer, DislikesSerializer
from rest_framework.authentication import TokenAuthentication


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)


# Comment like and dislike methods

    @action(detail=True, methods=['Get'])
    def user_liked(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        if CommentLikes.objects.filter(comment=comment, user=request.user):
            return Response({'like': 1}, status=status.HTTP_200_OK)
        else:
            return Response({'like': 0}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['Get'])
    def user_disliked(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        if CommentDislikes.objects.filter(comment=comment, user=request.user):
            return Response({'dislike': 1}, status=status.HTTP_200_OK)
        else:
            return Response({'dislike': 0}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def likes_list(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        likes = CommentLikes.objects.filter(comment=comment)
        serializer = LikesSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def dislikes_list(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        dislikes = CommentDislikes.objects.filter(comment=comment)
        serializer = DislikesSerializer(dislikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        user = request.user
        comment = Comment.objects.get(id=pk)
        try:
            CommentLikes.objects.get(user=user, comment=comment).delete()
            response = {'message': 'Your like was removed from this comment'}
            return Response(response, status=status.HTTP_200_OK)

        except:
            CommentLikes.objects.create(user=user, comment=comment)
            try:
                CommentDislikes.objects.get(user=user, comment=comment).delete()
                response = {'message': 'You liked the comment and Dislike was removed'}
                return Response(response, status=status.HTTP_200_OK)
            except:
                response = {'message': 'You liked the comment'}
                return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def dislike(self, request, pk=None):
        user = request.user
        comment = Comment.objects.get(id=pk)
        try:
            CommentDislikes.objects.get(user=user, comment=comment).delete()
            response = {'message': 'Your dislike was removed from this comment'}
            return Response(response, status=status.HTTP_200_OK)

        except:
            CommentDislikes.objects.create(user=user, comment=comment)
            try:
                CommentLikes.objects.get(user=user, comment=comment).delete()
                response = {'message': 'You disliked the comment and your like was removed'}
                return Response(response, status=status.HTTP_200_OK)
            except:
                response = {'message': 'You disliked the post'}
                return Response(response, status=status.HTTP_200_OK)

        # Post HTTP request methods

    def create(self, request, *args, **kwargs):
        user = request.user
        print(request.data)
        post_id = request.data['post_id']
        print(post_id)
        comment = request.data['comment']
        date = request.data['date']
        post = Post.objects.get(id=post_id)

        Comment.objects.create(user=user, post=post, comment=comment, date=date)
        return Response(status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        response = {'message': 'This method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        response = {'message': 'This method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        user = request.user
        post = Post.objects.get(id=pk)
        title = post.title

        if post.user_id == user.id:
            post.delete()
            response = {'message': 'Post with title "{0}" was deleted'.format(title)}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You can not delete another user post.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)

# Post like and dislike methods

    @action(detail=True, methods=['Get'])
    def user_liked(self, request, pk=None):
        post = Post.objects.get(id=pk)
        if Likes.objects.filter(post=post, user=request.user):
            return Response({'like': 1}, status=status.HTTP_200_OK)
        else:
            return Response({'like': 0}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['Get'])
    def user_disliked(self, request, pk=None):
        post = Post.objects.get(id=pk)
        if Dislikes.objects.filter(post=post, user=request.user):
            return Response({'dislike': 1}, status=status.HTTP_200_OK)
        else:
            return Response({'dislike': 0}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def likes_list(self, request, pk=None):
        post = Post.objects.get(id=pk)
        likes = Likes.objects.filter(post=post)
        serializer = LikesSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def dislikes_list(self, request, pk=None):
        post = Post.objects.get(id=pk)
        dislikes = Dislikes.objects.filter(post=post)
        serializer = DislikesSerializer(dislikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        user = request.user
        post = Post.objects.get(id=pk)
        try:
            Likes.objects.get(user=user, post=post).delete()
            response = {'message': 'Your like was removed from this post'}
            return Response(response, status=status.HTTP_200_OK)

        except:
            Likes.objects.create(user=user, post=post)
            try:
                Dislikes.objects.get(user=user, post=post).delete()
                response = {'message': 'You liked the post and Dislike was removed'}
                return Response(response, status=status.HTTP_200_OK)
            except:
                response = {'message': 'You liked the post'}
                return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def dislike(self, request, pk=None):
        user = request.user
        post = Post.objects.get(id=pk)
        try:
            Dislikes.objects.get(user=user, post=post).delete()
            response = {'message': 'Your dislike was removed from this post'}
            return Response(response, status=status.HTTP_200_OK)

        except:
            Dislikes.objects.create(user=user, post=post)
            try:
                Likes.objects.get(user=user, post=post).delete()
                response = {'message': 'You disliked the post and your like was removed'}
                return Response(response, status=status.HTTP_200_OK)
            except:
                response = {'message': 'You disliked the post'}
                return Response(response, status=status.HTTP_200_OK)


# Comments list

    @action(detail=True, methods=['GET'])
    def comment_list(self, request, pk=None):
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Post HTTP request methods

    def create(self, request, *args, **kwargs):
        user = request.user
        title = request.data['title']
        star_id = request.data['star']
        photo = request.data['photo']
        date = request.data['date']
        locationY = request.data['locationY']
        locationX = request.data['locationX']
        n18 = request.data['n18']

        star = Star.objects.get(id=star_id)

        Post.objects.create(user=user,
                            title=title,
                            star=star,
                            photo=photo,
                            date=date,
                            locationY=locationY,
                            locationX=locationX,
                            n18=n18)
        response = {'message': 'Post with title {0} for {1} was created'.format(title, star)}
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        response = {'message': 'This method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        response = {'message': 'This method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        user = request.user
        post = Post.objects.get(id=pk)
        title = post.title

        if post.user_id == user.id:
            post.delete()
            response = {'message': 'Post with title "{0}" was deleted'.format(title)}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You can not delete another user post.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

