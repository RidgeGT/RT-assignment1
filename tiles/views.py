from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
from .models import Tile

# Create your views here.
class ProfileListView(ListView):
    model = Tile
    template_name = 'tiles/home.html'
    context_object_name = 'tiles'