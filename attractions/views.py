from django.shortcuts import render, get_object_or_404
from .models import Attraction

def attraction_list(request):
    attractions = Attraction.objects.all()
    return render(request, 'attractions/attraction_list.html', {'attractions': attractions})

def attraction_detail(request, pk):
    attraction = get_object_or_404(Attraction, pk=pk)
    return render(request, 'attractions/attraction_detail.html', {'attraction': attraction})

