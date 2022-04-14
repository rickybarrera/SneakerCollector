from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.forms import CleaningForm
from .models import Cleaning, Sneaker
# Create your views here.\
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneakers_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {'sneakers': sneakers })
    
def sneakers_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    cleaning_form = CleaningForm()
    return render(request, 'sneakers/detail.html', { 'sneaker': sneaker, 'cleaning_form': cleaning_form })

class SneakerCreate(CreateView):
    model = Sneaker
    fields = '__all__'
    success_url = '/sneakers/'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['brand', 'description', 'release']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'

def add_cleaning(request, sneaker_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.sneaker_id = sneaker_id
        new_cleaning.save()
    return redirect('detail',sneaker_id=sneaker_id)