from django.urls import path
from .views import ProfileListView, ProfileListViewAge, ProfileListViewName
from . import views

urlpatterns = [
    path('',ProfileListView.as_view(),name = 'tiles_home'),
    path('sort/age',ProfileListViewAge.as_view(),name = 'tiles_age'),
    path('sort/username',ProfileListViewName.as_view(),name = 'tiles_name')
]