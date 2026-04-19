from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

# Create your views here.
@login_required
def students(request: HttpRequest) -> HttpResponse:
    return render(request, 'students/students.html')