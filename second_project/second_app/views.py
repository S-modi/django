from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dic={'insert_me':"USE SETTING FOR MORE INFORMATION"}
    return render(request,'index.html',context=my_dic)
