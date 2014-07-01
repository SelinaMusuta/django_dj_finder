from django.http import HttpResponse
from django.template import RequestContext, loader

from find_dj.models import DJ

# Create your views here.
def index(request):
	latest_dj_list = DJ.objects.all()
	template = loader.get_template('find_dj/index.html')
	context = RequestContext(request, { 'latest_dj_list': latest_dj_list,})
	return HttpResponse(template.render(context))

def index(request):
	dj_view = DJ.objects.get(dj_name='indanile')
	template = loader.get_template('find_dj/dj_view.html')
	context = RequestContext(request, { 'dj_view': dj_view,})
	return HttpResponse(template.render(context))