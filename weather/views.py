from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):

    if request.method == 'POST':
        location = request.POST.get('location')
        f = requests.get('http://api.weatherapi.com/v1/current.json?key=fe357202f9e24fcc85c122649221908&q={}&aqi=no'.format(location))

        result = json.loads(f.text)

        region = result['location']['name']
        country = result['location']['country']
        condition = result['current']['condition']['text']
        time = result['location']['localtime']
        
        context = {
            "location":location,
            "region":region,
            "country": country,
            "condition": condition,
            "time": time
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')