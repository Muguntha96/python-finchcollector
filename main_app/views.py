from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from .models import Finch,Toy
from .forms import FeedingForm
# Create your views here.

class Home(LoginView):
  template_name='home.html'

def about(request):
  return render(request,'about.html')

def finch_index(request):
  finches = Finch.objects.all()
  return render(request,'finches/index.html',{'finches':finches})

def finch_detail(request,finch_id):
  finch = Finch.objects.get(id=finch_id)
  toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request,'finches/detail.html',{'finch': finch,'feeding_form':feeding_form,'toys':toys_finch_doesnt_have})

class FinchCreate(CreateView):
  model = Finch
  fields = ['name','breed','description','age']
  success_url = '/finches/'
  def form_valid(self,form):
    form.instance.user=self.request.user
    return super().form_valid(form)

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

class ToyDetail(DetailView):
  model = Toy
  
class ToyList(ListView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name','color']

class ToyDelete(DeleteView):
  model = Toy
  success_url ='/toys/'

def assec_toy(request,finch_id,toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finch-detail',finch_id=finch_id)