from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from .utils import get_github_profile

# Create your views here.
class HomeView(generic.View):
  
  def get(self, request, **kwargs):
    username = request.GET.get("username")
    if username:
      user = get_github_profile(username)
      print(user.username)
      return render(request, "github/result.html", {"user": user})
    return render(request, "github/home.html")