from typing import List

import numpy as np

from genetic_algorithm.chromosomes.candidate import Candidate
from genetic_algorithm.fitnessfunctions.fitness_function import FitnessFunction
from genetic_algorithm.selections.selection import Selection


class RouletteWheelSelection(Selection):

    def select(self, population: List[Candidate], num_select: int, fitness_function: FitnessFunction):
        total_fitness = sum(fitness_function.compute(candidate) for candidate in population)
        selection_probs = [fitness_function.compute(candidate) / total_fitness for candidate in population]
        selected_indices = np.random.choice(len(population), size=num_select, replace=False, p=selection_probs)
        return [population[i] for i in selected_indices]
