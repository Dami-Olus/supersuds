from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.
from .models import Car
from .forms import RequestForm

def home(request):
    return render(request, 'main_app/home_page.html')

def index(request):
    return HttpResponse("Hello, world")

def detail(request, car_id):
    car = Car.objects.get(id=car_id)
    request_form = RequestForm()
    return render(request, 'main_app/car_detail.html', {'car': car, 'request_form': request_form})

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'color', 'licence']
   
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'car_id': self.object.id})
    
class CarUpdate(UpdateView):
    model=Car
    fields = ['make', 'model', 'color', 'licence']

class CarDelete(DeleteView):
    model = Car
    success_url = '/main_app/cars'

def car_list(request):
    cars = Car.objects.all()
    # template = loader.get_template('main_app/index.html')
    # context = {
    #     'cars': cars,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request, 'main_app/index.html', {'cars': cars})

def create_request(request, car_id):
    form = RequestForm(request.POST)
    if form.is_valid():
      new_request = form.save(commit=False)
      new_request.car_id = car_id
      new_request.save()
    return redirect('detail', car_id=car_id)