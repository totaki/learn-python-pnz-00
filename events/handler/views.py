from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from handler.serializers import EventsSerializer, PlaceSerializer, TagsSerializer, PrivatePlaceSerializer
from handler.models import Event, Place, Tag, User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User as Auth_User


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventsSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PrivatePlaceView(generics.GenericAPIView):
    """
    API endpoint that allows places current user's to be viewed.
    """

    def post(self, requests):
        user_token = self.request.data['token']
        # user_token = '1852fcf45e9f15c4f10f59553bfb49fa09af2e8b'
        token = Token.objects.get(key=user_token)
        auth_user_id = token.user_id
        auth_user = Auth_User.objects.get(id=auth_user_id)
        bot_user = User.objects.get(user_id=auth_user)
        place = Place.objects.get(owner=bot_user)
        return Response(place.place_name)

    serializer_class = PrivatePlaceSerializer

class TagsViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows tags to be viewed.
    """
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


