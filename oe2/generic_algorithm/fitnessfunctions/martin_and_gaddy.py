from oe2.generic_algorithm.fitnessfunctions.fitness_function import FitnessFunction


class MartinAndGaddyFunction(FitnessFunction):
    def compute(self, x):
        term1 = (x[0] - x[1]) ** 2
        term2 = (x[0] + x[1] - 10) ** 2 / 3
        return term1 + term2
