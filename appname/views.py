from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def appmain(request):
# write your python code
	return render(request, 'appname/myapp.html')