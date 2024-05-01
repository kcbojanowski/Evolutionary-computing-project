import random
from typing import List

from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome
from real_genetic_algorithm.crossovers.real_rossover import RealCrossover


class LinearCrossover:
    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> List[RealChromosome]:
        alpha1, alpha2, alpha3 = 0.25, 0.50, 0.25

        children: List[RealChromosome] = []
        x = []
        y = []
        z = []

        for i in range(len(chromosome1.real_representation)):
            x.append(alpha1 * chromosome1.real_representation[i] + alpha2 * chromosome2.real_representation[i])
            y.append(alpha2 * chromosome1.real_representation[i] + alpha3 * chromosome2.real_representation[i])
            z.append(alpha3 * chromosome1.real_representation[i] + alpha1 * chromosome2.real_representation[i])

        children.append(RealChromosome(x, fitness_function))
        children.append(RealChromosome(y, fitness_function))
        children.append(RealChromosome(z, fitness_function))

        return children
