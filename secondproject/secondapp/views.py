from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def greating_funnction(request):

	s1="<center><h1 style='color:green'>GOOD NIGHT</h1></center>"
	date=datetime.now()
	output=s1+"the server time is:"+str(date)
	return HttpResponse(output)


	
