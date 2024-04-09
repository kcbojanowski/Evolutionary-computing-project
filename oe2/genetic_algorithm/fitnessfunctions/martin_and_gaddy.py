from oe2.genetic_algorithm.chromosomes.candidate import Candidate
from oe2.genetic_algorithm.fitnessfunctions.fitness_function import FitnessFunction


class MartinAndGaddyFunction(FitnessFunction):
    def compute(self, candidate: Candidate):
        if len(candidate.chromosomes) != 2:
            raise ValueError("Calculate MartinAndGaddyFunction possible only for 2 dimensions")
        x = [chromosome.value for chromosome in candidate.chromosomes]
        term1 = (x[0] - x[1]) ** 2
        term2 = (x[0] + x[1] - 10) ** 2 / 3
        return term1 + term2
