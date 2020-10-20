from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    Webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':Webpages_list}
    #my_dict = {'insert_me':"Hello I am from views.py!"}
    return render(request,'first_app/index.html',context=date_dict)
