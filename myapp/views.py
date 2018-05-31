from django.shortcuts import render
#placing template lib 
from django.template import loader  
# Create your views here.
from django.http import HttpResponse 
from django.db import connection
from myapp.models import mysql
# import pdb; pdb.set_trace() #for testing 
titles={
            'company':'Stashing words'
            
          
        }

def listToDict(listWithTuple):
    name=listWithTuple[0][1]
    adress=listWithTuple[0][3]
    dictionary=dict(name=name,adress=adress)
    return dictionary


def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  



def index(request):
    T=mysql()
   
    #import pdb; pdb.set_trace() #for testing 
    template=loader.get_template('index.html')  
   
    return HttpResponse(template.render(listToDict(T)))  



def signup(request):
    if 'First-Name' in request.GET and request.GET['First-Name']:
       p1 = request.GET['First-Name']

    
    template=loader.get_template('signup.html')  
    return HttpResponse(template.render(titles))  
    


