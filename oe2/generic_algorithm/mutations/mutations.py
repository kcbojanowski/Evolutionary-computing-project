from oe2.generic_algorithm.chromosomes.chromosome import Chromosome
import random

#prob has to be between 0 and 1

def boundary_mutation(chromosome: Chromosome, prob: float) -> Chromosome:
    if prob < 0 or prob > 1:
        raise ValueError("Probability must be between 0 and 1")
    if not isinstance(chromosome, Chromosome):
        raise ValueError("Chromosome must be an instance of Chromosome class")
    if random.uniform(0, 1) < prob:
        if random.choice([True, False]):
            chromosome.binary_representation[0] = 1 - chromosome.binary_representation[0]
        else:
            chromosome.binary_representation[-1] = 1 - chromosome.binary_representation[-1]
    return chromosome

def one_point_mutation(chromosome: Chromosome, prob: float) -> Chromosome:
    if prob < 0 or prob > 1:
        raise ValueError("Probability must be between 0 and 1")
    if not isinstance(chromosome, Chromosome):
        raise ValueError("Chromosome must be an instance of Chromosome class")
    if random.uniform(0, 1) < prob:
        i = random.randint(0, len(chromosome.binary_representation) - 1)
        chromosome.binary_representation[i] = 1 - chromosome.binary_representation[i]
    return chromosome

def two_point_mutation(chromosome: Chromosome, prob: float) -> Chromosome:
    if prob < 0 or prob > 1:
        raise ValueError("Probability must be between 0 and 1")
    if not isinstance(chromosome, Chromosome):
        raise ValueError("Chromosome must be an instance of Chromosome class")
    if random.uniform(0, 1) < prob:
        i = random.randint(0, len(chromosome.binary_representation) - 1)
        j = random.randint(0, len(chromosome.binary_representation) - 1)
        chromosome.binary_representation[i] = 1 - chromosome.binary_representation[i]
        chromosome.binary_representation[j] = 1 - chromosome.binary_representation[j]
    return chromosome

#write another boundary mutation function that flips the first and the last bit of the chromosome

