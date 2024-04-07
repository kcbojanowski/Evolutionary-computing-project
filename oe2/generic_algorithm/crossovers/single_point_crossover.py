import random

from crossover import Crossover
from oe2.generic_algorithm.chromosomes.chromosome import Chromosome


class SinglePointCrossover(Crossover):
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        Crossover.crossover(self, chromosome1, chromosome2)
        crossover_point = random.randint(0, len(chromosome1.binary_representation) - 1)
        child_binary_representation = chromosome1.binary_representation[0:crossover_point] + chromosome2.binary_representation[crossover_point:]
        return Chromosome(child_binary_representation, chromosome1.left_boundary, chromosome1.right_boundary)