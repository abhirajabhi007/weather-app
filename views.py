from django.shortcuts import render
import json
import urllib.request


def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        if city:
            try:
               source = urllib.request.urlopen( 
                   'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=45b01a7f6a9893cc9370a6fd91f105fb').read()
        
               list_of_data = json.loads(source) 

               data = { 
                  "country_code": str(list_of_data['sys']['country']), 
                  "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
                  "temp": str(list_of_data['main']['temp']) + 'k', 
                  "pressure": str(list_of_data['main']['pressure']), 
                  "humidity": str(list_of_data['main']['humidity']), 
               } 
           
            except Exception as e:
                
                data = {"error": "An error occurred while fetching weather data."}
        else:
            data = {"error": "Please enter a city name."}
    else:
        data = {}
    return render(request, "main/index.html", data)
