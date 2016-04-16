from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'otter/index.html', context)
    #return HttpResponse("navy blue otter app landing page2.")
# Create your views here.
