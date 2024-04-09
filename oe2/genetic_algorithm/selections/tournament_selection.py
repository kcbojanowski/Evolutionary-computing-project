import random
from typing import List

from genetic_algorithm.chromosomes.candidate import Candidate
from genetic_algorithm.fitnessfunctions.fitness_function import FitnessFunction
from genetic_algorithm.selections.selection import Selection


class TournamentSelection(Selection):
    def __init__(self, tournament_size: int, maximization: bool ):
        self.tournament_size = tournament_size
        self.maximization = maximization

    def select(self, population: List[Candidate], num_select: int, fitness_function: FitnessFunction):
        selected = []
        for _ in range(num_select):
            tournament = random.sample(population, self.tournament_size)
            if self.maximization:
                winner = max(tournament, key=lambda candidate: fitness_function.compute(candidate))
            else:
                winner = min(tournament, key=lambda candidate: fitness_function.compute(candidate))
            selected.append(winner)
        return selected
