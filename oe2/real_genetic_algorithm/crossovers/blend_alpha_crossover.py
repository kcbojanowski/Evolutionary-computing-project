import random
from typing import List

from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome
from real_genetic_algorithm.crossovers.real_rossover import RealCrossover

class BlendAlphaCrossover(RealCrossover):
    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> List[RealChromosome]:
        children: List[RealChromosome] = [] 
        alpha = 0.3
        x = []
        y = []

        for i in range(len(chromosome1.real_representation)):
            d = abs(chromosome1.real_representation[i] - chromosome2.real_representation[i])
            a = min(chromosome1.real_representation[i], chromosome2.real_representation[i]) - alpha * d
            b = max(chromosome1.real_representation[i], chromosome2.real_representation[i]) + alpha * d
            u_x = random.uniform(a, b)
            u_y = random.uniform(a, b)
            x.append(u_x)
            y.append(u_y)
        
        children.append(RealChromosome(x, fitness_function))
        children.append(RealChromosome(y, fitness_function))

        return children