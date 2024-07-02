from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('carpets/', views.CarpetListView.as_view(), name='carpet_list'),
    path('carpet/<slug:slug>/', views.CarpetDetailView.as_view(), name='carpet_detail'),
]