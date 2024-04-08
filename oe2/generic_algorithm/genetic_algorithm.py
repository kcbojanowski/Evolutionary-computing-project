import random
from typing import List

from oe2.generic_algorithm.chromosomes.chromosome import generate_chromosomes, Chromosome
from oe2.generic_algorithm.genetic_algorithm_configuration import GeneticAlgorithmConfiguration


class GeneticAlgorithm:
    def __init__(self, configuration: GeneticAlgorithmConfiguration):
        self.configuration = configuration

    def perform(self):
        population = generate_chromosomes(
            self.configuration.chromosome_count,
            self.configuration.chromosome_size,
            self.configuration.left_boundary,
            self.configuration.right_boundary
        )
        elite_chromosomes, rest_chromosomes = GeneticAlgorithm.elite_strategy(population,
                                                                              self.configuration.elite_chromosome_count)
        selected_chromosomes = self.configuration.selection.select(rest_chromosomes,
                                                                   self.configuration.selection_count)  # nie wiem czy z populacji calej czy tylko z reszty

        new_population = self.create_new_population(selected_chromosomes)
        new_population.extend(elite_chromosomes)

    def create_new_population(self, chromosomes: List[Chromosome]) -> List[Chromosome]:
        new_population = []
        new_population_size = self.configuration.chromosome_count - self.configuration.elite_chromosome_count
        while len(new_population) < new_population_size:
            left, right = random.sample(chromosomes, 2)  # sample czy choice ???
            if random.random() < self.configuration.crossover_rate:
                new_population.append(self.configuration.crossover.crossover(left, right))

        return new_population

    @staticmethod
    def elite_strategy(population: List[Chromosome], num_select: int) -> tuple[List[Chromosome], List[Chromosome]]:
        """
        Split chromosomes to chosen ones and the rest of them

        Args:
        - population
        - num_select: Number of chromosomes or percentage if use_percentage=True.
        - use_percentage: Defines if num_select is number of percentage

        Returns:
        - Tuple with selected chromosomes and the rests of them
        """

        sorted_population = sorted(population, key=lambda chromosome: chromosome.fitness, reverse=True)
        selected = sorted_population[:num_select]
        remaining = sorted_population[num_select:]

        return selected, remaining
