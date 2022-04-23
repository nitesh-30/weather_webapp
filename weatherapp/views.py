from django.shortcuts import render
import urllib.request
import json 
# Create your views here.
def index(request):
    data={}
    if request.method=='POST':
        city=request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=72d9e3f84c525753f38d9018e50b358f')
        json_data=json.load(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate_code":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
    else:
        city=''
        data={}
    return render(request, 'index.html', {'city':city,'data':data})

   