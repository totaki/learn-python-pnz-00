from django.urls import path, include
from rest_framework import routers
from handler.views import EventViewSet, PlaceViewSet


router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'places', PlaceViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls))
]
