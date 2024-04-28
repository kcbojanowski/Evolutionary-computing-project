import random
import statistics
from typing import List, Tuple

from timeit import default_timer as timer

from real_genetic_algorithm.real_genetic_algorithm_configuration import RealGeneticAlgorithmConfiguration
from real_genetic_algorithm.chromosomes.real_chromosome import generate_real_chromosomes


class RealGeneticAlgorithm:
    def __init__(self, configuration: RealGeneticAlgorithmConfiguration):
        self.configuration = configuration

    def perform(self):
        # Initialize population
        population = generate_real_chromosomes(self.configuration.population_size, self.configuration.chromosome_dimension, self.configuration.left_boundary, self.configuration.right_boundary, self.configuration.fitness_function)

        for _ in range(self.configuration.generations):
            # Select parents
            parents = self.configuration.selection_method.select(population)

            # Generate offspring through crossover
            offspring = [self.configuration.crossover_method.crossover(p1, p2) for p1, p2 in zip(parents[::2], parents[1::2])]

            # Perform mutation
            offspring = [self.configuration.mutation_method.mutation(child, self.configuration.mutation_probability) for child in offspring]

            # Evaluate fitness
            for individual in offspring:
                individual.calculate_value()

            # Select for the next generation
            population = self.configuration.selection_method.select(population + offspring)

        # Return the best solution
        return max(population, key=lambda individual: individual.calculate_value())