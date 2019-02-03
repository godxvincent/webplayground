from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from registration.models import Profile

# Create your views here.


class ProfileListView(ListView):
    model = Profile


class ProfileDetailView(DetailView):
    model = Profile

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
