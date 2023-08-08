from .forms import RegForm
from django.views import View
from django.shortcuts import render
from script.getVehicle import getVehicleData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class HomeView(View):
    def get(self, request):
        return render(self.request, 'home.html', {})

@csrf_exempt
def vehicleData(request):
    if request.method == 'POST':
            model, make, year = 'N/A', 'N/A', 'N/A'
            data = json.load(request)
            reg = data['reg']
            try:
                model, make, year = getVehicleData(reg)
            except:
                 print('Not valid number plate')
                 pass
            return JsonResponse({
                 'message': 'success',
                'model': model,
                'make': make,
                'year': year,
            })


