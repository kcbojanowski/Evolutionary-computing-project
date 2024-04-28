import random
from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome


class RealMutation:
    def mutation(self, chromosome: RealChromosome, prob: float) -> RealChromosome:
        raise NotImplementedError("Choose subclass")


class GaussMutation(RealMutation):
    def mutation(self, chromosome: RealChromosome, prob: float) -> RealChromosome:
        new_representation = []
        for gene in chromosome.real_representation:
            if random.random() < prob:
                gene += random.gauss(0, 1)
            new_representation.append(gene)
        return RealChromosome(new_representation, chromosome.fitness_function)


class UniformMutation(RealMutation):
    def mutation(self, chromosome: RealChromosome, prob: float) -> RealChromosome:
        new_representation = []
        for gene in chromosome.real_representation:
            if random.random() < prob:
                gene = random.uniform(-1, 1)
            new_representation.append(gene)
        return RealChromosome(new_representation, chromosome.fitness_function)