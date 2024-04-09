import random

from oe2.genetic_algorithm.chromosomes.chromosome import Chromosome
from oe2.genetic_algorithm.crossovers.crossover import Crossover


class StableCrossover(Crossover):
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        child_binary_representation = []
        parent_a = chromosome1.binary_representation
        parent_b = chromosome2.binary_representation
        for i in range(len(chromosome1.binary_representation)):
            if parent_a[i] == parent_b[i]:
                child_binary_representation.append(parent_b[i])
            else:
                u = random.random()
                if i <= 0.5:
                    child_binary_representation.append(0)
                else:
                    child_binary_representation.append(1)

        return Chromosome(child_binary_representation, chromosome1.left_boundary, chromosome1.right_boundary)
