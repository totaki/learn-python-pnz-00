from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from handler.serializers import EventsSerializer, PlaceSerializer, TagsSerializer, PrivatePlaceSerializer, MeSerializer
from handler.models import Event, Place, Tag, User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User as Auth_User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


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


class PrivatePlaceView(viewsets.ModelViewSet):
    """
    API endpoint that allows places current user's to be viewed.
    """
    serializer_class = PrivatePlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'user') and user.user:
            return Place.objects.filter(owner=user.user)
        elif user and user.is_staff:
            return Place.objects.filter()
        else:
            raise PermissionDenied()

    def create(self, request, *args, **kwargs):
        request._data = {**request.data, 'owner': request.user.user.id}
        return super().create(request, *args, **kwargs)


class TagsViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows tags to be viewed.
    """
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class MeView(viewsets.ReadOnlyModelViewSet):

    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.user
