from django.http import Http404
from django.shortcuts import render, get_object_or_404

from find_dj.models import DJ

# Create your views here.
def index(request):
	latest_dj_list = DJ.objects.all()
	return render(request, 'find_dj/index.html', { 'latest_dj_list': latest_dj_list})

def dj_view(request, dj_id):
	dj = get_object_or_404(DJ, pk= dj_id)
	return render(request, 'find_dj/dj_view.html', { 'dj': dj})