from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import connection
# Create your views here.
def test(request):
    template = loader.get_template("master.html")
    return HttpResponse(template.render())

# print("-----------test start")
# # template = loader.get_template("test.html")
# # with connection.cursor() as cursor:
# #     cursor.execute("update myprofile_About set website='dddddddddddd' where id=1")
# #     row = cursor.fetchone()

# from . models import About
# qset = About.objects.raw("Select * from myprofile_About where id=2")
# for a in qset:
#     print(a)

print("-----------test start")

def querytest(request):
    template = loader.get_template("test.html")
    with connection.cursor() as cursor:
        cursor.execute("update myprofile_About set website='ooooooooo' where id=1")
        row = cursor.fetchone()

    

    return HttpResponse(template.render())