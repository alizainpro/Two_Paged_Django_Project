from django.shortcuts import render

# Create your views here.
def index(request):
    DATA = {'websites':[{'url':'http://google.com','name':'Google'},{'url':'http://microsoft.com','name':'Microsoft'},{'url':'http://djangoproject.com','name':'Django Project'}]}
    return render(request,"firstapp/index.html",context=DATA)
def details(request):
    DATA = {'companies':[{'contact':'support@google.com','name':'Google'},{'contact':'contact@microsoft.com','name':'Microsoft'},{'contact':'support@djangoproject.com','name':'Django Project'}]}
    return render(request,"firstapp/details.html",context=DATA)