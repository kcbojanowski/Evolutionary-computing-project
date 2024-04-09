import random
import statistics
from typing import List, Tuple

from genetic_algorithm.chromosomes.candidate import generate_candidates, Candidate
from genetic_algorithm.genetic_algorithm_configuration import GeneticAlgorithmConfiguration
from genetic_algorithm.inversion.inv import inversion
from timeit import default_timer as timer


class GeneticAlgorithm:
    def __init__(self, configuration: GeneticAlgorithmConfiguration):
        self.configuration = configuration

    def perform(self):
        population = generate_candidates(
            self.configuration.dimensions,
            self.configuration.chromosome_count,
            self.configuration.chromosome_size,
            self.configuration.left_boundary,
            self.configuration.right_boundary
        )

        best_candidate_values = []
        average_epoch_values = []
        standard_deviations = []

        best_candidate = Candidate(None)

        start = timer()
        for epoch in range(self.configuration.epochs_amount):
            elite_candidates, rest_candidates = self.elite_strategy(population,
                                                                    self.configuration.elite_chromosome_count)

            all_fitness_vals = [self.configuration.fitness_function.compute(candidate)
                                for candidate in population]

            best_candidate = elite_candidates[0]
            best_candidate_values.append(self.configuration.fitness_function.compute(elite_candidates[0]))
            average_epoch_values.append(sum(all_fitness_vals) / len(all_fitness_vals))
            standard_deviations.append(statistics.stdev(all_fitness_vals))

            selected_candidates = self.configuration.selection.select(population,
                                                                      self.configuration.selection_count,
                                                                      self.configuration.fitness_function)

            population = self.create_new_population(selected_candidates)
            population = [self.mutated_candidate(candidate) for candidate in population]
            population = [self.inverted_candidate(candidate) for candidate in population]
            population.extend(elite_candidates)
        end = timer()
        algorithm_time = end - start

        # print(algorithm_time)
        print(best_candidate_values)
        # print(average_epoch_values)
        # print(standard_deviations)

        best_arguments = [chromosome.value for chromosome in best_candidate.chromosomes]

        return best_candidate_values, average_epoch_values, standard_deviations, algorithm_time, best_arguments
        
    def mutated_candidate(self, candidate: Candidate):
        return Candidate(
            [self.configuration.mutation.mutation(chromosome, self.configuration.mutation_rate) for chromosome in
             candidate.chromosomes])

    def inverted_candidate(self, candidate: Candidate):
        return Candidate(
            [inversion(chromosome, self.configuration.mutation_rate) for chromosome in
             candidate.chromosomes])

    def create_new_population(self, candidates: List[Candidate]) -> List[Candidate]:
        new_population = []
        new_population_size = self.configuration.chromosome_count - self.configuration.elite_chromosome_count
        while len(new_population) < new_population_size:
            left, right = random.sample(candidates, 2)  # sample czy choice ???
            if random.random() < self.configuration.crossover_rate:
                new_population.append(self.configuration.crossover.crossover_candidates(left, right))

        return new_population

    def elite_strategy(self, population: List[Candidate], num_select: int) -> Tuple[List[Candidate], List[Candidate]]:
        """
        Split chromosomes to chosen ones and the rest of them

        Args:
        - population
        - num_select: Number of chromosomes or percentage if use_percentage=True.
        - use_percentage: Defines if num_select is number of percentage

        Returns:
        - Tuple with selected chromosomes and the rests of them
        """
        sorted_population = sorted(population,
                                   key=lambda candidate: self.configuration.fitness_function.compute(candidate))  #TODO min/max -> reverse
        selected = sorted_population[:num_select]
        remaining = sorted_population[num_select:]

        return selected, remaining
