from django.urls import path
from . import views

urlpatterns = [
    # ex: /handler/
    path('', views.index, name='index'),
    path('place/', views.place, name='place')
]
