import random

from crossover import Crossover
from oe2.generic_algorithm.chromosomes.chromosome import Chromosome


class ThreePointCrossover(Crossover):
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        Crossover.crossover(self, chromosome1, chromosome2)
        crossover_points = random.sample(range(len(chromosome1.binary_representation)), 3)
        crossover_points.sort()
        print(crossover_points)
        child_binary_representation = (
                chromosome1.binary_representation[:crossover_points[0]] +
                chromosome2.binary_representation[crossover_points[0]:crossover_points[1]] +
                chromosome1.binary_representation[crossover_points[1]:crossover_points[2]] +
                chromosome2.binary_representation[crossover_points[2]:]
        )
        return Chromosome(child_binary_representation, chromosome1.left_boundary, chromosome1.right_boundary)
