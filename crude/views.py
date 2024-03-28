from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.

def create(request):
    print("this ispost")
    template = loader.get_template("crude.html")
    return HttpResponse(template.render())


def read(self):
    pass

def update(self):
    pass
def delete(self):
    pass