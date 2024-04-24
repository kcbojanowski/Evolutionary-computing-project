import random
from typing import List

from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome
from real_genetic_algorithm.crossovers.real_rossover import RealCrossover

class ArithmeticCrossover(RealCrossover):
    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> List[RealChromosome]:
        alpha = 0.25
        children: List[RealChromosome] = []
        x = []
        y = []
        for i in range(len(chromosome1.real_representation)):
            x.append(alpha * chromosome1.real_representation[i] + (1-alpha)*chromosome2.real_representation[i])
            y.append(alpha * chromosome2.real_representation[i] + (1-alpha)*chromosome1.real_representation[i])
       
        children.append(RealChromosome(x, fitness_function))
        children.append(RealChromosome(y, fitness_function))
    
        return children

    
