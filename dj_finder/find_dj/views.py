from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, dancers.  You're entering the dj universe.")