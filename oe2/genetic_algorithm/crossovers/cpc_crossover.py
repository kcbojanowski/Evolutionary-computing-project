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

        for i in range(l_length):
            if random.random() < 0.5:
                if l_up:
                    pos_lup = l_up[i]
                    child_1[pos_lup], child_2[pos_lup] = child_2[pos_lup], child_1[pos_lup]
                if l_down:
                    pos_ldown = l_down[i]
                    child_1[pos_ldown], child_2[pos_ldown] = child_2[pos_ldown], child_1[pos_ldown]

        return Chromosome(child_1, chromosome1.left_boundary, chromosome1.right_boundary)
