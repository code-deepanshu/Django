from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
def home(request):
    return HttpResponse("Welcome to the Task Manager!")


