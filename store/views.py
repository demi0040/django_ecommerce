from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Carpet

class CarpetListView(ListView):
    model = Carpet
    template_name = 'store/carpet_list.html'
    context_object_name = 'carpets'
    paginate_by = 12

class CarpetDetailView(DetailView):
    model = Carpet
    template_name = 'store/carpet_detail.html'
    context_object_name = 'carpet'

def home(request):
    featured_carpets = Carpet.objects.filter(is_active=True)[:4]
    return render(request, 'store/home.html', {'featured_carpets': featured_carpets})