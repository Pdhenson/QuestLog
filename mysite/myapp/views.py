from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        "body":"CINS465 Hello World!",
        "title":"Assignment 3 Hello World!",
        "next":"Next",
    }
    return render(request, "base.html", context=context)
