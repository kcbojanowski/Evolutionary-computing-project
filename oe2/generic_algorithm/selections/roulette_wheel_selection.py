import numpy as np

from oe2.generic_algorithm.selections.selection import SelectionMethod


class RouletteWheelSelection(SelectionMethod):

    def select(self, population, num_select):
        total_fitness = sum(chromosome.fitness for chromosome in population)
        selection_probs = [chromosome.fitness / total_fitness for chromosome in population]
        selected_indices = np.random.choice(len(population), size=num_select, replace=False, p=selection_probs)
        return [population[i] for i in selected_indices]