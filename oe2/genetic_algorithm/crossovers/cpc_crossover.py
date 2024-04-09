import random

from genetic_algorithm.crossovers.crossover import Crossover
from genetic_algorithm.chromosomes.chromosome import Chromosome


class CpcCrossover(Crossover):
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        Crossover.crossover(self, chromosome1, chromosome2)

        l_up, l_down = [], []
        l_length = 0

        for i in range(len(chromosome1.binary_representation)):
            if chromosome1.binary_representation[i] > chromosome2.binary_representation[i]:
                l_up.append(i)
                l_length += 1
            elif chromosome1.binary_representation[i] < chromosome2.binary_representation[i]:
                l_down.append(i)

        child_1 = chromosome1.binary_representation.copy()
        child_2 = chromosome2.binary_representation.copy()

        for i in l_up:
            if random.random() < 0.5:
                child_1[i], child_2[i] = child_2[i], child_1[i]

        for i in l_down:
            if random.random() < 0.5:
                child_1[i], child_2[i] = child_2[i], child_1[i]

        return Chromosome(child_1, chromosome1.left_boundary, chromosome1.right_boundary)
