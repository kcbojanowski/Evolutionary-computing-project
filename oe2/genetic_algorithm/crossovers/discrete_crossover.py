import random

from genetic_algorithm.chromosomes.chromosome import Chromosome
from genetic_algorithm.crossovers.crossover import Crossover


class DiscreteCrossover(Crossover):
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        pass