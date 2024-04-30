from django.shortcuts import render, redirect

# uAyFTC8/NExfa2z+V232Ow==WDYIPDfopOFcGONp
# Create your views here.
from django.shortcuts import render
import requests
import json
    

def home(request):
    context = {'error': ''}
    if request.method == 'GET' and 'clear' in request.GET:
        if 'cars' in request.session:
            del request.session['cars']

    if request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        year = request.POST.get('year')

        if make and model and year:
            api_url = f'https://api.api-ninjas.com/v1/cars?make={make}&model={model}&year={year}&limit=50'
            try:
                api_request = requests.get(api_url, headers={'X-Api-Key': 'uAyFTC8/NExfa2z+V232Ow==WDYIPDfopOFcGONp'})
                api_request.raise_for_status()
                cars = json.loads(api_request.content)

                if not cars:
                    context['cars'] = None
                    context['error'] = "No cars found for the specified make, model, and year."
                else:
                    request.session['cars'] = cars
                    context['cars'] = cars

            except requests.exceptions.HTTPError as e:
                context['error'] = f"HTTP error occurred: {e}"
            except Exception as e:
                context['error'] = f"An error occurred: {e}"
        else:
            context['error'] = "Please enter make, model, and year"
        pass
    else:
        # Clearing the session data when accessing the home page through a GET request
        context['cars'] = request.session.get('cars', None)
    return render(request, "home.html", context)



       

 
# Remaining views
def about(request):
    return render(request, 'about.html')

def car_detail(request, make, model, year):
    
    api_url = f'https://api.api-ninjas.com/v1/cars?make={make}&model={model}&year={year}'
    response = requests.get(api_url, headers={'X-Api-Key': 'uAyFTC8/NExfa2z+V232Ow==WDYIPDfopOFcGONp'})
    cars = response.json()
    car = next((c for c in cars if str(c['year']) == str(year)), None)

    if not car:
        return render(request, 'car_not_found.html')
    
    return render(request, 'car_detail.html', {'car': car})

def back_to_list(request):
    return redirect('home')