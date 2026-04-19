from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

# Create your views here.
@login_required
def courses(request: HttpRequest) -> HttpResponse:
    return render(request, 'courses/courses.html')
