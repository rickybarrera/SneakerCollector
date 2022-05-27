from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from main_app.forms import CleaningForm
import boto3 
import uuid
import os
from .models import Cleaning, Sneaker, Lace, Photo
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

    id_list = sneaker.laces.all().values_list('id')
    laces_sneaker_doesnt_have = Lace.objects.exclude(id__in=id_list)
    cleaning_form = CleaningForm()
    return render(request, 'sneakers/detail.html', { 'sneaker': sneaker, 'cleaning_form': cleaning_form, 'laces': laces_sneaker_doesnt_have })


def add_photo(request, sneaker_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  print(photo_file)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    print(f"this is the key - {key}")
    # just in case something goes wrong
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      print (f"this is the bucket - {bucket}")
      # build the full url string
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      print(f"this is the url - {url}")
      # we can assign to sneaker_id or sneaker (if you have sneaker object)
      Photo.objects.create(url=url, sneaker_id=sneaker_id)
      print(f"this is the photo{Photo}")
    except Exception as error:
      print('An error occurred uploading file to S3')
      print(f"this is the errpr{error}")
  return redirect('detail', sneaker_id=sneaker_id)

def assoc_lace(request,sneaker_id, lace_id):
    Sneaker.objects.get(id=sneaker_id).laces.add(lace_id)
    return redirect('detail', sneaker_id=sneaker_id)
class SneakerCreate(CreateView):
    model = Sneaker
    fields = ['name', 'brand', 'description', 'release']
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

class LaceList(ListView):
    model = Lace

class LaceDetail(DetailView):
    model = Lace

class LaceCreate(CreateView):
    model = Lace
    fields = '__all__'

class LaceUpdate(UpdateView):
    model = Lace
    fields = ['name', 'color']

class LaceDelete(DeleteView):
    model = Lace
    success_url = '/laces/'


