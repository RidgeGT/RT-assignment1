from django.urls import path
from .views import ProfileListView
from . import views

urlpatterns = [
    path('',ProfileListView.as_view(),name = 'tiles_home')
]