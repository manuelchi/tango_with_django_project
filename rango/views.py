from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #Linea inicial:
    #return HttpResponse("Rango says hey there! <br/> <a href='/rango/about/'>About</a> ")
    context_dict = {'boldmessage': 'crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    

def about(request):
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Main page</a>")