from django.contrib.auth.views import LogoutView
from django.urls import path

from main_app import admin
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/',views.about,name='about'),
  path('finches/',views.finch_index,name='finch-index'),
  path('finches/<int:finch_id>/',views.finch_detail,name='finch-detail'),
  path('finches/create/',views.FinchCreate.as_view(),name='finch-create'),
  path('finches/<int:pk>/update',views.FinchUpdate.as_view(),name='finch-update'),
  path('finches/<int:pk>/delete',views.FinchDelete.as_view(),name='finch-delete'),
  path('finches/<int:finch_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/',views.ToyCreate.as_view(),name='toy-create'),
  path('toys/<int:pk>/',views.ToyDetail.as_view(),name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/',views.ToyUpdate.as_view(),name='toy-update'),
  path('toys/<int:pk>/delete/',views.ToyDelete.as_view(),name='toy-delete'),
  path('finches/<int:finch_id>/assec-toy/<int:toy_id>/', views.assec_toy, name='assec-toy'),
  # path('logout/', LogoutView.as_view(), name='logout'),
  path('accounts/signup/', views.signup, name='signup')
  ] 