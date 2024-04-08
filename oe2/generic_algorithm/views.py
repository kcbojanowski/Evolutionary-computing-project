
import time
from django.shortcuts import render

def index(request):
    if request.method == 'GET':
    
        return render(request, 'generic.html')

    
    elif request.method == 'POST':

        print("DUPA")    
        function = request.POST.get('function')
        range_start = float(request.POST.get('range-start'))
        range_end = float(request.POST.get('range-end'))
        population_size = int(request.POST.get('population-size'))
        chromosome_length = int(request.POST.get('chromosome-length'))
        epochs_amount = int(request.POST.get('epochs-amount'))
        elite_amount = int(request.POST.get('elite-amount'))
        chromosome_amount = int(request.POST.get('chromosome-amount'))
        crossover_rate = float(request.POST.get('crossover-rate'))
        mutation_probability = float(request.POST.get('mutation-rate'))
        inversion_rate = float(request.POST.get('inversion-rate'))
        selection_method = request.POST.get('selection-method')
        crossover_method = request.POST.get('crossover-method')
        mutation_method = request.POST.get('mutation-method')
        maximization = bool(request.POST.get('maximization', False))

        time.sleep(10)

        return render(request, 'generic.html')