from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

import matplotlib
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from matplotlib import pyplot as plt
from datetime import *
import io

from real_genetic_algorithm.crossovers.arithmetic_crossover import ArithmeticCrossover
from real_genetic_algorithm.crossovers.average_crossover import AverageCrossover
from real_genetic_algorithm.crossovers.blend_alpha_beta_crossover import BlendAlphaBetaCrossover
from real_genetic_algorithm.crossovers.blend_alpha_crossover import BlendAlphaCrossover
from real_genetic_algorithm.crossovers.linear_crossover import LinearCrossover
from real_genetic_algorithm.crossovers.king_stratrgy_crossover import KingStrategyCrossover
from real_genetic_algorithm.crossovers.center_of_gravity_crossover import CenterOfGravityCrossover
from real_genetic_algorithm.models import RealGeneticAlgorithmResult
from real_genetic_algorithm.mutations.real_mutations import GaussMutation, UniformMutation
from real_genetic_algorithm.real_genetic_algorithm import RealGeneticAlgorithm
from real_genetic_algorithm.real_genetic_algorithm_configuration import RealGeneticAlgorithmConfiguration
from real_genetic_algorithm.selections.real_selection import RealBestSelection, RealRouletteWheelSelection, RealTournamentSelection

matplotlib.use('agg')


def index(request):
    return redirect('real_genetic_algorithm', permanent=True)

def real_genetic_algorithm(request):
    if request.method == 'GET':
        latest_result = RealGeneticAlgorithmResult.objects.order_by('-date').first()
        if latest_result:
            return render(request, 'real_genetic.html', {'latest_result': latest_result})
        else:
            return render(request, 'real_genetic.html')

    elif request.method == 'POST':
        result = RealGeneticAlgorithmResult(
            function = request.POST.get('function'),
            range_start = float(request.POST.get('range-start')),
            range_end = float(request.POST.get('range-end')),
            population_size = int(request.POST.get('population-size')),
            chromosome_dimension = int(request.POST.get('chromosome-dimension')),
            epochs_amount = int(request.POST.get('epochs-amount')),
            elite_amount = int(request.POST.get('elite-amount')),
            selection_amount = int(request.POST.get('selection-amount')),
            crossover_rate = float(request.POST.get('crossover-rate')),
            mutation_rate = float(request.POST.get('mutation-rate')),
            inversion_rate = float(request.POST.get('inversion-rate')),
            selection_method = request.POST.get('selection-method'),
            crossover_method = request.POST.get('crossover-method'),
            mutation_method = request.POST.get('mutation-method'),
            maximization = bool(request.POST.get('maximization', False)),
            total_time=None,
            pdf_file=None,
        )

        print(result)

        fitness_function = result.function
        crossover = chooseCrossoverMethod(result.crossover_method)
        mutation = chooseMutationMethod(result.mutation_method)
        selection = chooseSelectionMethod(result.selection_method, result.selection_amount, result.maximization)

        algorithm_config = RealGeneticAlgorithmConfiguration(
            fitness_function=fitness_function, ##remember that fitnessfunction is a string now
            crossover=crossover,
            mutation=mutation,
            selection=selection,
            left_boundary=result.range_start,
            right_boundary=result.range_end,
            dimensions=result.chromosome_dimension,
            population_size=result.population_size,
            epochs_amount=result.epochs_amount,
            elite_chromosome_count=result.elite_amount,
            crossover_rate=result.crossover_rate,
            mutation_rate=result.mutation_rate,
            inversion_rate=result.inversion_rate,
            selection_count=result.selection_amount,
            maximization=result.maximization
        )

        algorithm = RealGeneticAlgorithm(algorithm_config)

        graph1_data, graph2_data, graph3_data, result.total_time, best_arguments = algorithm.perform() ##total time do

        pdf_file = generate_pdf(graph1_data, graph2_data, graph3_data, best_arguments, result)
        result.pdf_file.save(f"{result.function}.pdf", ContentFile(pdf_file), save=True)
        result.save()

        return render(request, 'genetic.html')

def generate_pdf(data1, data2, data3, best_arguments, result):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    y = 750
    c.setFont("Helvetica", 16)
    c.drawString(100, y, "Algorithm Configuration:")
    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(100, y, f"Function: {result.function}")
    y -= 20
    c.drawString(100, y, f"Range Start: {result.range_start}")
    y -= 20
    c.drawString(100, y, f"Range End: {result.range_end}")
    y -= 20
    c.drawString(100, y, f"Population Size: {result.population_size}")
    y -= 20
    c.drawString(100, y, f"Chromosome Dimension: {result.chromosome_dimension}")
    y -= 20
    c.drawString(100, y, f"Epochs Amount: {result.epochs_amount}")
    y -= 20
    c.drawString(100, y, f"Elite Strategy amount: {result.elite_amount}")
    y -= 20
    c.drawString(100, y, f"Best and tournament chromosome amount: {result.selection_amount}")
    y -= 20
    c.drawString(100, y, f"Crossover rate: {result.crossover_rate}")
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
    y -= 40

    c.setFont("Helvetica", 16)
    if result.maximization:
        c.drawString(100, y, f"Maximum Value: {data1[len(data1)-1]}")
        y -= 20
        c.drawString(100, y, f"Arguments : {best_arguments}")
    else:
        c.drawString(100, y, f"Minimum Value: {data1[len(data1)-1]}")
        y -= 30
        c.drawString(100, y, f"Arguments : {best_arguments}")

    c.showPage()
    y = 730
    c.setFont("Helvetica", 16)
    c.drawString(100, y, f"Graphs:")
    y -= 300

    indices = range(len(data1))

    plt.plot(indices, data1)
    plt.xlabel('Epoch')
    plt.ylabel('Best Value')
    plt.title('Dependence of the Best Function Value on the Epoch')
    plt.grid(True)
    plt.savefig('plot1.png', format='png')
    plt.close()
    c.drawImage('plot1.png', 100, y, width=400, height=300)

    y -= 350

    plt.plot(indices, data2)
    plt.xlabel('Epoch')
    plt.ylabel('Average Value')
    plt.title('Dependence of the Average Function Value on the Epoch')
    plt.grid(True)
    plt.savefig('plot2.png', format='png')
    plt.close()
    c.drawImage('plot2.png', 100, y, width=400, height=300)

    c.showPage()
    y = 400
    plt.plot(indices, data3)
    plt.xlabel('Epoch')
    plt.ylabel('Standard Deviations Value')
    plt.title('Dependence of the Standard deviation Value on the Epoch')
    plt.grid(True)
    plt.savefig('plot3.png', format='png')
    plt.close()
    c.drawImage('plot3.png', 100, y, width=400, height=300)

    c.save()
    pdf_content = buffer.getvalue()
    buffer.close()
    return pdf_content



def chooseCrossoverMethod(method_name):
    match method_name:
        case 'arithmetic':
            return ArithmeticCrossover()
        case 'average':
            return AverageCrossover()
        case 'alfa':
            return BlendAlphaCrossover()
        case 'alfa-beta':
            return BlendAlphaBetaCrossover()
        case 'linear':
            return LinearCrossover()
        case 'king-strategy':
            return KingStrategyCrossover(None)
        case 'center-of-gravity':
            return CenterOfGravityCrossover()

def chooseMutationMethod(method_name):
    match method_name:
        case 'uniform':
            return UniformMutation()
        case 'gauss':
            return GaussMutation()


def chooseSelectionMethod(method_name, chromosome_amout, maximization ):
    match method_name:
        case 'best':
            return RealBestSelection()
        case 'roulette':
            return RealRouletteWheelSelection()
        case 'tournament':
            return RealTournamentSelection(chromosome_amout, maximization)




