import io
from django.utils import timezone
from datetime import *
from django.shortcuts import render, redirect

from genetic_algorithm.models import GeneticAlgorithmResult
from django.core.files.base import ContentFile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from genetic_algorithm.crossovers.discrete_crossover import DiscreteCrossover
from genetic_algorithm.crossovers.single_point_crossover import SinglePointCrossover
from genetic_algorithm.crossovers.three_point_crossover import ThreePointCrossover
from genetic_algorithm.crossovers.two_point_crossover import TwoPointCrossover
from genetic_algorithm.crossovers.uniform_crossover import UniformCrossover
from genetic_algorithm.fitnessfunctions.ackley import AckleyFunction
from genetic_algorithm.fitnessfunctions.martin_and_gaddy import MartinAndGaddyFunction
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm.genetic_algorithm_configuration import GeneticAlgorithmConfiguration
from genetic_algorithm.mutations.mutations import BoundaryMutation, OnePointMutation, TwoPointMutation
from genetic_algorithm.selections.roulette_wheel_selection import RouletteWheelSelection
from genetic_algorithm.selections.tournament_selection import TournamentSelection


def index(request):
    if request.method == 'GET':
        latest_result = GeneticAlgorithmResult.objects.all()
        if latest_result:
            return render(request, 'genetic.html', {'latest_result': latest_result[0]})
        else:
            return render(request, 'genetic.html')
    
    elif request.method == 'POST':
        result = GeneticAlgorithmResult(
            function = request.POST.get('function'),
            range_start = float(request.POST.get('range-start')),
            range_end = float(request.POST.get('range-end')),
            population_size = int(request.POST.get('population-size')),
            chromosome_length = int(request.POST.get('chromosome-length')),
            epochs_amount = int(request.POST.get('epochs-amount')),
            elite_amount = int(request.POST.get('elite-amount')),
            chromosome_amount = int(request.POST.get('chromosome-amount')),
            crossover_rate = float(request.POST.get('crossover-rate')),
            mutation_rate = float(request.POST.get('mutation-rate')),
            inversion_rate = float(request.POST.get('inversion-rate')),
            selection_method = request.POST.get('selection-method'),
            crossover_method = request.POST.get('crossover-method'),
            mutation_method = request.POST.get('mutation-method'),
            maximization = bool(request.POST.get('maximization', False)),
            average_time=None,
            maximum_time=None,
            pdf_file=None,
        )


        fitness_function = chooseFitnessFunction(result.function)
        dimension = 2,
        crossover = chooseCrossoverMethod(result.crossover_method)
        mutation = chooseMutationMethod(result.mutation_method)
        selection = chooseSelectionMethod(result.selection_method, result.selection_method)

        algorith_config = GeneticAlgorithmConfiguration(
            fitness_function=fitness_function, 
            crossover=crossover, 
            mutation=mutation, 
            selection=selection,
            left_boundary=result.range_start,
            right_boundary=result.range_end,
            dimensions=dimension,
            chromosome_count=result.population_size,
            chromosome_size=result.chromosome_length,
            epochs_amount=result.epochs_amount,
            elite_chromosome_count=result.elite_amount,
            crossover_rate=result.crossover_rate,
            mutation_rate=result.mutation_rate,
            inversion_rate=result.inversion_rate,
            selection_count=result.chromosome_amount,
        )
        algorithm = GeneticAlgorithm(algorith_config)

        graph1_data, graph2_data, result.average_time, result.maximum_time = algorithm.perform()
        
        print(graph1_data, graph2_data)

        pdf_file = generate_pdf(0, 0, result)
        result.pdf_file.save(f"{result.function}.pdf", ContentFile(pdf_file), save=True)
        result.save()

        return render(request, 'genetic.html')
    
def generate_pdf(data1, data2, result):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 16)
    y = 750
    c.drawString(100, y, "Algorithm Configuration:")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(100, y, f"Function: {result.function}")
    y -= 20
    c.drawString(100, y, f"Range Start: {result.range_start}")
    y -= 20
    c.drawString(100, y, f"Range End: {result.range_end}")
    y -= 20
    c.drawString(100, y, f"Population Size: {result.population_size}")
    y -= 20
    c.drawString(100, y, f"Chromosome Length: {result.chromosome_length}")
    y -= 20
    c.drawString(100, y, f"Epochs Amount: {result.epochs_amount}")
    y -= 20
    c.drawString(100, y, f"Elite Strategy amount: {result.elite_amount}")
    y -= 20
    c.drawString(100, y, f"Best and tournament chromosome amount: {result.chromosome_amount}")
    y -= 20
    c.drawString(100, y, f"Crosover rate: {result.crossover_rate}")
    y -= 20
    c.drawString(100, y, f"Mutation rate: {result.mutation_rate}")
    y -= 20
    c.drawString(100, y, f"Inversion rate: {result.inversion_rate}")
    y -= 20
    c.drawString(100, y, f"Selection method: {result.selection_method}")
    y -= 20
    c.drawString(100, y, f"Crossover method: {result.crossover_method}")
    y -= 20
    c.drawString(100, y, f"Mutation method: {result.mutation_method}")
    y -= 20
    c.drawString(100, y, f"Maximalization: {result.maximization}")
    y -= 20
    c.save()
    pdf_content = buffer.getvalue()
    buffer.close()
    return pdf_content

def generate_graphs(data1,data2):
    pass

def chooseFitnessFunction(function_name):
    if function_name == '':
        return MartinAndGaddyFunction()
    elif function_name == '':
        return AckleyFunction()
    
def chooseCrossoverMethod(method_name):
    match method_name:
        case 'one-point':
            return SinglePointCrossover()
        case 'two-point':
            return TwoPointCrossover()
        case 'three-point':
            return ThreePointCrossover()
        case 'discrete-point':
            return DiscreteCrossover()
        case 'uniform':
            return UniformCrossover()
        
def chooseMutationMethod(method_name):
    match method_name:
        case 'one-point':
            return OnePointMutation()
        case 'two-point':
            return TwoPointMutation()
        case 'boundary':
            return BoundaryMutation()

def chooseSelectionMethod(method_name, chromosome_amout ):
    match method_name:
        case 'best':
            return TournamentSelection(chromosome_amout)
        case 'roulette':
            return RouletteWheelSelection()
        case 'tournament':
            return TournamentSelection(chromosome_amout)
       
       
    
   
