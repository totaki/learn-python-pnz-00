from django.urls import path, include
from rest_framework import routers
from handler.views import EventViewSet, PlaceViewSet, PrivatePlaceView, TagsViewSet


router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'tags', TagsViewSet)


urlpatterns = [
    path('api/v1/public/', include(router.urls)),
    path('api/v1/private/places', PrivatePlaceView.as_view()),
]
