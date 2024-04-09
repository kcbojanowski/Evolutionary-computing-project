import numpy as np

from genetic_algorithm.chromosomes.candidate import Candidate
from genetic_algorithm.fitnessfunctions.fitness_function import FitnessFunction


class AckleyFunction(FitnessFunction):
    def compute(self, candidate: Candidate):
        x = np.array([chromosome.value for chromosome in candidate.chromosomes])
        dimensions = len(x)
        sum_sq = np.sum(x ** 2)
        sum_cos = np.sum(np.cos(2 * np.pi * x))
        term1 = -20 * np.exp(-0.2 * np.sqrt(sum_sq / dimensions))
        term2 = -np.exp(sum_cos / dimensions)
        return term1 + term2 + 20 + np.e
