import random
from typing import List

from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome
from real_genetic_algorithm.crossovers.real_rossover import RealCrossover

class LinearCrossover(RealCrossover):
    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> List[RealChromosome]:
        children: List[RealChromosome] = []
        chromosome1 = RealChromosome([2,2], '')
        chromosome2 = RealChromosome([3,3], '')
        z = []
        v = []
        w = []
        for i in range(len(chromosome1.real_representation)):
            z.append(chromosome1.real_representation[i] / 2 + chromosome2.real_representation[i] / 2)
            v.append(3 * chromosome1.real_representation[i] / 2 - chromosome2.real_representation[i] / 2)
            w.append(-chromosome1.real_representation[i] / 2 + 3 * chromosome2.real_representation[i] / 2)
        
        child_z = RealChromosome(z, fitness_function)
        child_v = RealChromosome(v, fitness_function)
        child_w = RealChromosome(w, fitness_function)

        worst_chromosome_value = min(child_z.value, child_v.value, child_w.value)
        if child_z.value != worst_chromosome_value: children.append(child_z)
        if child_v.value != worst_chromosome_value: children.append(child_v)
        if child_w.value != worst_chromosome_value: children.append(child_w)

        return children
