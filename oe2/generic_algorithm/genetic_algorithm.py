import random
from typing import List, Tuple

from oe2.generic_algorithm.chromosomes.candidate import generate_candidates, Candidate
from oe2.generic_algorithm.genetic_algorithm_configuration import GeneticAlgorithmConfiguration
from oe2.generic_algorithm.inversion.inv import inversion


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
        best = 100
        x = 100
        y = 100

        for epoch in range(self.configuration.epochs_amount):
            elite_candidates, rest_candidates = self.elite_strategy(population,
                                                                    self.configuration.elite_chromosome_count)

            best = self.configuration.fitness_function.compute(elite_candidates[0])
            x = elite_candidates[0]

            selected_candidates = self.configuration.selection.select(rest_candidates,
                                                                      self.configuration.selection_count,
                                                                      self.configuration.fitness_function)  # nie wiem czy z populacji calej czy tylko z reszty

            population = self.create_new_population(selected_candidates)
            population = [self.mutated_candidate(candidate) for candidate in population]
            population = [self.inverted_candidate(candidate) for candidate in population]
            population.extend(elite_candidates)
        print(best)
        for a in x.chromosomes:
            print(a.value)

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
                                   key=lambda candidate: self.configuration.fitness_function.compute(candidate))
        selected = sorted_population[:num_select]
        remaining = sorted_population[num_select:]

        return selected, remaining
