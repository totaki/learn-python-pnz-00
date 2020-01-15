from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'places', views.PlaceViewSet)
# router.register(r'setevent', views.SetEventView)


urlpatterns = [
    # ex: /handler/
    path('', views.index, name='index'),
    path('place/', views.place, name='place'),
    path('api/v1/', include(router.urls))
]
