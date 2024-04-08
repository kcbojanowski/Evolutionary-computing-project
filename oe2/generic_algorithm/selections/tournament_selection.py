import random
from typing import List

from oe2.generic_algorithm.chromosomes.candidate import Candidate
from oe2.generic_algorithm.fitnessfunctions.fitness_function import FitnessFunction
from oe2.generic_algorithm.selections.selection import Selection


class TournamentSelection(Selection):
    def __init__(self, tournament_size: int):
        self.tournament_size = tournament_size

    def select(self, population: List[Candidate], num_select: int, fitness_function: FitnessFunction):
        selected = []
        for _ in range(num_select):
            tournament = random.sample(population, self.tournament_size)
            winner = min(tournament, key=lambda candidate: fitness_function.compute(candidate))  #TODO min/max
            selected.append(winner)
        return selected
