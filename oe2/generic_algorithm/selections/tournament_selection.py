import numpy as np

from oe2.generic_algorithm.selections.selection import SelectionMethod


class TournamentSelection(SelectionMethod):

    def select(self, population, num_select, tournament_size=3):
        selected = []
        for _ in range(num_select):
            tournament = np.random.choice(population, size=tournament_size, replace=False)
            winner = max(tournament, key=lambda chromosome: chromosome.fitness)
            selected.append(winner)
        return selected