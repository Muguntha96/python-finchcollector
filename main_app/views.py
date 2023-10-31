from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Finch
# Create your views here.


def finch_index(request):
  finches = Finch.objects.all()
  return render(request,'finches/index.html',{'finches':finches})

def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def finch_detail(request,finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request,'finches/detail.html',{'finch': finch})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/'
  