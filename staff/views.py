from django.shortcuts import render
from .models import Staff

# Create your views here.

def home(request):
	# return render(request,'base.html')
	return render(request,'staff/base.html')