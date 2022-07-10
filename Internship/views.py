from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category="
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['alldata'] = inshorts_data
    return render(request, 'index.html', records)

def aboutus(request):
    return render(request, 'aboutus.html')

def page(request):
    return render(request, '404.html')

def footer(request):
    return render(request, '_footer.html')

def navbar(request):
    return render(request, '_nevbar.html')

def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['entertainmentdata'] = inshorts_data
    return render(request, 'entertainment.html', records)

def startup(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=startup"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['startupdata'] = inshorts_data
    return render(request, 'startup.html', records)

def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['businessdata'] = inshorts_data
    return render(request, 'business.html', records)

def contactus(request):
    return render(request, 'contactus.html')

def technology(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=technology"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['technologydata'] = inshorts_data
    return render(request, 'technology.html', records)

def politics(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=politics"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['politicsdata'] = inshorts_data
    return render(request, 'politics.html', records)

def automobile(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=automobile"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['automobiledata'] = inshorts_data
    return render(request, 'automobile.html', records)

def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def travel(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=travel"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['traveldata'] = inshorts_data
    return render(request, 'travel.html', records)

def world(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=world"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['worlddata'] = inshorts_data
    return render(request, 'world.html', records)