from django.shortcuts import render
from datetime import datetime

# Create your views here.
def Wish_django(request):
	date=datetime.now()
	msg='i am proud to be an indian'
	my_dict={'date':date,'msg':msg}
	return render('request'sixthapp/display.html',context=my_dict)