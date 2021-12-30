
from django.shortcuts import render
from .models import Place
# Create your views here.

def index(request):
    latest_matjip_list = Place.objects.order_by('-name')[:5]
    context = {'latest_matjip_list': latest_matjip_list}
    return render(request, 'matjip/index.html', context)