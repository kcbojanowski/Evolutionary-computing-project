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
        population = generate_real_chromosomes(self.configuration.population_size,
                                               self.configuration.chromosome_dimension,
                                               self.configuration.left_boundary, self.configuration.right_boundary,
                                               self.configuration.fitness_function)

        best_candidate_values = []
        average_epoch_values = []
        standard_deviations = []
        best_candidate = self.calculate_best_value(population)
        start = timer()
        for _ in range(self.configuration.epochs_amount):
            # Select parents
            parents = self.configuration.selection.select(population, self.configuration.selection_count,
                                                          self.configuration.fitness_function,
                                                          self.configuration.maximization)

            # Generate offspring through crossover
            offspring = []
            for p1, p2 in zip(parents[::2], parents[1::2]):
                offspring.extend(self.configuration.crossover.crossover(p1, p2, self.configuration.fitness_function))

            # Perform mutation
            offspring = [self.configuration.mutation.mutation(child, self.configuration.mutation_rate) for child in
                         offspring]

            # Evaluate fitness
            for individual in offspring:
                individual.calculate_value()

            # Select for the next generation
            population = self.configuration.selection.select(population + offspring,
                                                             self.configuration.selection_count,
                                                             self.configuration.fitness_function,
                                                             self.configuration.maximization)

            current_best = self.calculate_best_value(population)
            if self.configuration.maximization:
                best_candidate = current_best if current_best.calculate_value() > best_candidate.calculate_value() else best_candidate
            else:
                best_candidate = current_best if current_best.calculate_value() < best_candidate.calculate_value() else best_candidate

            best_candidate_values.append(best_candidate.calculate_value())
            average_epoch_values.append(self.calculate_mean_value(population))
            standard_deviations.append(self.calculate_std_value(population))

        end = timer()
        algorithm_time = end - start

        best_arguments = best_candidate.real_representation

        # Return the best solution
        return best_candidate_values, average_epoch_values, standard_deviations, algorithm_time, best_arguments

    def calculate_best_value(self, population):
        if self.configuration.maximization:
            return max(population, key=lambda individual: individual.calculate_value())
        else:
            return min(population, key=lambda individual: individual.calculate_value())

    def calculate_mean_value(self, population):
        return sum(individual.calculate_value() for individual in population) / len(population)

    def calculate_std_value(self, population):
        return statistics.pstdev([individual.calculate_value() for individual in population])
