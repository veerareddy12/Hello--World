from django.shortcuts import render
from datetime import datetime

# Create your views here.
def greetings_django(request):
	date = datetime.now()
	msg = 'Good Afternoon'
	my_dict = {'date':date,'msg':msg}
	return render(request,'thirdapp/display.html',context=my_dict)