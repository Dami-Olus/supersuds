from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
from .models import Car

def home(request):
    return render(request, 'main_app/home_page.html')

def index(request):
    return HttpResponse("Hello, world")

def detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'main_app/car_detail.html', {'car': car})

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'color', 'licence']
   
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'car_id': self.object.id})

def car_list(request):
    cars = Car.objects.all()
    # template = loader.get_template('main_app/index.html')
    # context = {
    #     'cars': cars,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request, 'main_app/index.html', {'cars': cars})