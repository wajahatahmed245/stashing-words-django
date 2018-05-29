from django.shortcuts import render
#placing template lib 
from django.template import loader  
# Create your views here.
from django.http import HttpResponse  

titles={
        'company':'Stashing words'
    }
    
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  



def index(request):
    template=loader.get_template('index.html')  
   
    return HttpResponse(template.render(titles))  



def signup(request):
    template=loader.get_template('signup.html')  
    return HttpResponse(template.render(titles))  
    