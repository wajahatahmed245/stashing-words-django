from django.shortcuts import render
#placing template lib 
from django.template import loader  
# Create your views here.
from django.http import HttpResponse  

def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  



def index(request):
    template=loader.get_template('index.html')  
    titles={
        'company':'Stashing words'
    }
    return HttpResponse(template.render(titles))  

    