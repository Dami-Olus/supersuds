from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Car

def home(request):
    return render(request, 'main_app/home_page.html')

def index(request):
    return HttpResponse("Hello, world")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def car_list(request):
    cars = Car.objects.all()
    # template = loader.get_template('main_app/index.html')
    # context = {
    #     'cars': cars,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request, 'main_app/index.html', {'cars': cars})