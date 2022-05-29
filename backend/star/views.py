
from rest_framework import viewsets, status
from rest_framework.response import Response

from star.models import Star, Followers
from star.serializer import StarSerializer, FollowersSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

from post.models import Post


class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        user = request.user
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        sex = request.data['first_name']
        country = request.data['country']
        celebrity = request.data['celebrity']

        try:
            star = Star.objects.get(first_name=first_name)
            if star.last_name == last_name:
                response = {'message': 'Star with name {0} {1} already exist'.format(first_name, last_name)}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except:
            Star.objects.create(user=user,
                                first_name=first_name,
                                last_name=last_name,
                                sex=sex,
                                country=country,
                                celebrity=celebrity)
            response = {'message': 'Star {0} {1} was created'.format(first_name, last_name)}
            return Response(response, status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        response = {'message': 'This method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        response = {'message': 'This method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        user = request.user
        star = Star.objects.get(id=pk)
        first_name = star.first_name
        last_name = star.last_name
        posts = Post.objects.filter(star=star)

        def check_for_other_user_posts():
            for post in posts:
                if post.user != user:
                    return False
            return True

        if star.user == user and check_for_other_user_posts() is True:
            star.delete()
            response = {'message': '{0} {1} was deleted'.format(first_name, last_name)}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You can not delete star created by another user, '
                                   'or if star have photos from another user.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


    def get_star_post_lenght(self, id):
        return len(Star.objects.get(id=id).posts)


class FollowersViewSet(viewsets.ModelViewSet):
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET'])
    def list_of_followers(self, request, pk=None):
        star = Star.objects.get(id=pk)
        list_of_followers = Followers.objects.filter(star=star)
        serializer = FollowersSerializer(list_of_followers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def list_of_following_stars(self, request):
        user = request.user
        list_of_following_users = Followers.objects.filter(follower=user)
        serializer = FollowersSerializer(list_of_following_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['Get'])
    def is_following(self, request, pk=None):
        user = request.user
        star_to_fallow = Star.objects.get(id=pk)
        if Followers.objects.filter(follower=user, star=star_to_fallow):
            return Response({'follow': 1}, status=status.HTTP_200_OK)
        else:
            return Response({'follow': 0}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def follow(self, request, pk=None):
        user = request.user
        star_to_fallow = Star.objects.get(id=pk)
        try:
            Followers.objects.get(follower=user, star=star_to_fallow).delete()
            response = {'message': 'You unfollowed star: {0} {1}'.format(star_to_fallow.first_name, star_to_fallow.last_name)}
            return Response(response, status=status.HTTP_200_OK)
        except:
            Followers.objects.create(follower=user, star=star_to_fallow)
            response = {'message': 'You started to follow star: {0} {1}'.format(star_to_fallow.first_name, star_to_fallow.last_name)}
            return Response(response, status=status.HTTP_200_OK)


