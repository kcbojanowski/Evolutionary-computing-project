import random
from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome

def inversion(chromosome: RealChromosome, prob: float, left_boundary: float, right_boundary: float) -> RealChromosome:
    new_representation = chromosome.real_representation.copy()
    for i in range(len(new_representation)):
        if random.random() < prob:
            mid_point = (left_boundary + right_boundary) / 2
            new_representation[i] = mid_point * 2 - new_representation[i]
    return RealChromosome(new_representation, chromosome.fitness_function)
