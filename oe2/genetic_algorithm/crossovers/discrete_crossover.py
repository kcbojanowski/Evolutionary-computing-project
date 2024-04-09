import random

from genetic_algorithm.chromosomes.chromosome import Chromosome
from genetic_algorithm.crossovers.crossover import Crossover


class DiscreteCrossover(Crossover):
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        child_binary_representation = []
        for i in range(len(chromosome1.binary_representation)):
            if random.random() <= 0.5:
                child_binary_representation.append(chromosome1.binary_representation[i])
            else:
                child_binary_representation.append(chromosome2.binary_representation[i])
        return Chromosome(child_binary_representation, chromosome1.left_boundary, chromosome1.right_boundary)
