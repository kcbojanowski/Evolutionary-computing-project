from typing import List

from genetic_algorithm.chromosomes.candidate import Candidate
from genetic_algorithm.fitnessfunctions.fitness_function import FitnessFunction


class Selection:

    def select(self, population: List[Candidate], num_select: int, fitness_function: FitnessFunction):
        """
        Selects chromosomes from populaction

        Args:
        - population: list of chromosomes
        - num_select: Number of chromosomes to select

        Returns:
        - List of selected chromosomes
        """
        raise NotImplementedError("Implement select() method in subclass")