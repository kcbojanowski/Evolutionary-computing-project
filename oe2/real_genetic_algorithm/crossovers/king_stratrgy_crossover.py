import random
from typing import List

from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome
from real_genetic_algorithm.crossovers.real_rossover import RealCrossover


class KingStrategyCrossover:
    def __init__(self, king: RealChromosome):
        self.king = king

    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> List[RealChromosome]:
        child_genes = [(g1 + g2) / 2 for g1, g2 in zip(self.king.real_representation, chromosome1.real_representation)]
        child = RealChromosome(child_genes, fitness_function)
        return [child]
