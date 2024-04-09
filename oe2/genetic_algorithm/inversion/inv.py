from genetic_algorithm.chromosomes.chromosome import Chromosome
import random

#prob has to be between 0 and 1

def inversion(chromosome: Chromosome, prob: float) -> Chromosome:
    if prob < 0 or prob > 1:
        raise ValueError("Probability must be between 0 and 1")
    if not isinstance(chromosome, Chromosome):
        raise ValueError("Chromosome must be an instance of Chromosome class")
    if random.uniform(0,1) < prob:
        i = random.randint(0, len(chromosome.binary_representation) - 1)
        j = random.randint(0, len(chromosome.binary_representation) - 1)
        if i > j:
            i, j = j, i
        chromosome.binary_representation = chromosome.binary_representation[:i] + chromosome.binary_representation[i:j+1][::-1] + chromosome.binary_representation[j+1:]
    return chromosome