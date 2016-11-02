from django.shortcuts import render
from django.http import HttpResponse

# criar a view
def index(request):
    return render(request,'index.html',{})

def OlaMundo(request):
    return HttpResponse("Olá mundo!")

def status_code(request):
    return HttpResponse("Resposta %s" % (HttpResponse.status_code))