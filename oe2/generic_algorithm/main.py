import random

from chromosomes.chromosome import generate_chromosomes
from chromosomes.chromosome import Chromosome
from oe2.generic_algorithm.crossovers.single_point_crossover import SinglePointCrossover
from oe2.generic_algorithm.elite_strategy import RouletteWheelSelection, EliteStrategy

CHROMOSOME_COUNT = 20
SELECTION_COUNT = 10

CHROMOSOME_SIZE = 10
LEFT_BOUNDARY = -10
RIGHT_BOUNDARY = -10
ELITE_CHROMOSOME_COUNT = 2

CROSSOVER_RATE = 0.7

EPOCHS_AMOUNT = 100

crossover = SinglePointCrossover()

population = generate_chromosomes(CHROMOSOME_COUNT, CHROMOSOME_SIZE, LEFT_BOUNDARY, RIGHT_BOUNDARY)



elite_strategy = EliteStrategy()
elite_chromosomes, rest_chromosomes = elite_strategy.select_and_split(population, ELITE_CHROMOSOME_COUNT)
new_population = elite_chromosomes

selection = RouletteWheelSelection()
selected_chromosomes = selection.select(population, SELECTION_COUNT) # nie wiem czy z populacji calej czy tylko z reszty


while len(new_population) < CHROMOSOME_COUNT:
    left, right = random.sample(selected_chromosomes, 2)  # sample czy choice ???
    if random.random() < CROSSOVER_RATE:
        new_population.append(crossover.crossover(left, right))
