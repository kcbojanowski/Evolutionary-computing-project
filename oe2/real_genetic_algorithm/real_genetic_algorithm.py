import statistics
import random

from timeit import default_timer as timer

from real_genetic_algorithm.real_genetic_algorithm_configuration import RealGeneticAlgorithmConfiguration
from real_genetic_algorithm.chromosomes.real_chromosome import generate_real_chromosomes
from real_genetic_algorithm.inversion.real_inversion import inversion
from real_genetic_algorithm.crossovers.king_stratrgy_crossover import KingStrategyCrossover

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
            # Select elite
            elite_individuals = self.elite_strategy(population, self.configuration.elite_chromosome_count)

            # Select parents
            parents = self.configuration.selection.select(population, self.configuration.selection_count,
                                                          self.configuration.fitness_function,
                                                          self.configuration.maximization)

            offspring = self.create_new_population(parents, best_candidate)

            # Perform mutation
            offspring = [self.configuration.mutation.mutation(child, self.configuration.mutation_rate) for child in
                         offspring]

            # Perform inversion
            offspring = [inversion(child, self.configuration.mutation_rate, self.configuration.left_boundary,
                                   self.configuration.right_boundary) for child in offspring]

            # Evaluate fitness
            for individual in offspring:
                individual.calculate_value()

            offspring.extend(elite_individuals)
            population = offspring

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

    def create_new_population(self, candidates, best_candidate):
        new_population = []
        new_population_size = self.configuration.population_size - self.configuration.elite_chromosome_count
        if isinstance(self.configuration.crossover, KingStrategyCrossover):
            self.configuration.crossover = KingStrategyCrossover(best_candidate)
        while len(new_population) < new_population_size:
            left, right = random.sample(candidates, 2)
            if random.random() < self.configuration.crossover_rate:
                new_population.extend(
                    self.configuration.crossover.crossover(left, right, self.configuration.fitness_function))
        return new_population

    def elite_strategy(self, population, num_select: int):
        sorted_population = sorted(population,
                                   key=lambda individual: individual.calculate_value(),
                                   reverse=self.configuration.maximization)
        selected = sorted_population[:num_select]
        return selected
