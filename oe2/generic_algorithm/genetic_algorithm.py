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
        elite_chromosomes, rest_chromosomes = GeneticAlgorithm.elite_strategy(population, self.configuration.elite_chromosome_count)

        # new_population = elite_chromosomes
        #
        # selected_chromosomes = self.configuration.selection.select(population, self.configuration.selection_count)  # nie wiem czy z populacji calej czy tylko z reszty
        #
        # while len(new_population) < CHROMOSOME_COUNT:
        #     left, right = random.sample(selected_chromosomes, 2)  # sample czy choice ???
        #     if random.random() < CROSSOVER_RATE:
        #         new_population.append(crossover.crossover(left, right))

    def create_new_population(self):


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
