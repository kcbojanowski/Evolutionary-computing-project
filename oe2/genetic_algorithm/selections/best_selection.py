import random
from typing import List

from oe2.genetic_algorithm.chromosomes.candidate import Candidate
from oe2.genetic_algorithm.fitnessfunctions.fitness_function import FitnessFunction
from oe2.genetic_algorithm.selections.selection import Selection


class BestSelection(Selection):

    def select(self, population: List[Candidate], num_select: int, fitness_function: FitnessFunction):
        sorted_population = sorted(population,
                                   key=lambda candidate: fitness_function.compute(candidate))  #TODO min/max
        selected = sorted_population[:num_select]
        return selected
