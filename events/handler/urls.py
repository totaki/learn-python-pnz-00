from django.urls import path, include
from rest_framework import routers
from handler.views import EventViewSet, PlaceViewSet, PrivatePlaceView, TagsViewSet, MeView, PrivateEventView

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'tags', TagsViewSet)


urlpatterns = [
    path('api/v1/public/', include(router.urls)),
    path('api/v1/private/me', MeView.as_view({'get': 'retrieve'})),
    path('api/v1/private/places', PrivatePlaceView.as_view({
        'post': 'create',
        'get': 'list'
    })),
    path('api/v1/private/events', PrivateEventView.as_view({'post': 'create'}))
]
