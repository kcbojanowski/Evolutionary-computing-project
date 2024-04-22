import random
from typing import List

from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome
from real_genetic_algorithm.crossovers.real_rossover import RealCrossover

class AverageCrossover(RealCrossover):
    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> List[RealChromosome]:
        children = [] #List[RealChromosome]
        #TODO add crossover
        return children