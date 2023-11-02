from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Finch,Toy
from .forms import FeedingForm
# Create your views here.


def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def finch_index(request):
  finches = Finch.objects.all()
  return render(request,'finches/index.html',{'finches':finches})

def finch_detail(request,finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form = FeedingForm()
  # feedings = FeedingFinch.objects.filter(finch = finch)
  # feedings_count = Finch.feeding_set.all().count()
  # 'feedings':feedings
  return render(request,'finches/detail.html',{'finch': finch,'feeding_form':feeding_form})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['description','age']
  
class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def add_feeding(request,finch_id):
  if request.method == 'POST':
    form = FeedingForm(request.POST)
    if form.is_valid():
      new_feeding = form.save(commit = False)
      new_feeding.finch_id=finch_id
      new_feeding.save()
  return redirect('finch-detail',finch_id=finch_id)

class ToyCreate(CreateView):
  model = Toy
  fields= '__all__'