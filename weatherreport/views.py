from django.shortcuts import render

# Create your views here.
import requests

def fetch_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data

def gen(n):
    for i in range(n):
        #print(i)
        yield i

#print(help(gen(10)))

#print(gen(10))
#for i in gen(10):
#    print(i)


obj = gen(10)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
from functools import reduce
def some_task(a,b):
  return a+b


lst = [1,2,3,4,20]
print(reduce(some_task, lst))
