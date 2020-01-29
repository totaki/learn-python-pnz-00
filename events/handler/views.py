from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from handler.serializers import EventsSerializer, PlaceSerializer, TagsSerializer, PrivatePlaceSerializer, \
    PrivateEventSerializer
from handler.models import Event, Place, Tag, User
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from datetime import datetime


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    now = datetime.utcnow()
    queryset = Event.objects.filter(event_time__gte=now).order_by("event_time")
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
        request.data['owner'] = request.user.user.id
        return super().create(request, *args, **kwargs)


class PrivateEventView(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be added.
    """
    serializer_class = PrivateEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.all()

    def create(self, request, *args, **kwargs):
        place_from_req = request.data['place']
        place = Place.objects.get(place_name=place_from_req)
        request.data['place'] = place.id
        tags_from_req = request.data['tags']
        tags_for_create = []
        if isinstance(tags_from_req, str):
            tags = Tag.objects.get(title=tags_from_req)
            tags_for_create.append(tags.id)
        else:
            for tag in tags_from_req:
                tags = Tag.objects.get(title=tag)
                tags_for_create.append(tags.id)
        request.data['tags'] = tags_for_create
        return super().create(request, *args, **kwargs)


# Добавляю свой класс для Pagination чтобы теги выводились на страницу все сразу
class TagsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class TagsViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows tags to be viewed.
    """
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    pagination_class = TagsSetPagination  # использую особый класс
