from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
from .models import Tile

# Create your views here.
class ProfileListView(ListView):
    model = Tile
    template_name = 'tiles/home.html'
    context_object_name = 'tiles'

class ProfileListViewAge(ListView):
    model = Tile
    template_name = 'tiles/home.html'
    context_object_name = 'tiles'
    ordering = ['age']

class ProfileListViewName(ListView):
    model = Tile
    template_name = 'tiles/home.html'
    context_object_name = 'tiles'
    ordering = ['username']

class ProfileDetailView(DetailView):
    model = Tile