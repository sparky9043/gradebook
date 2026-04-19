from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/dashboard.html')