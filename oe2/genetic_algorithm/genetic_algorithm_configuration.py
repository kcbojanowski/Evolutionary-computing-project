from dataclasses import dataclass

from oe2.genetic_algorithm.crossovers.crossover import Crossover
from oe2.genetic_algorithm.fitnessfunctions.fitness_function import FitnessFunction
from oe2.genetic_algorithm.mutations.mutations import Mutation
from oe2.genetic_algorithm.selections.selection import Selection


class GeneticAlgorithmConfiguration:

    def __init__(self,
                 fitness_function: FitnessFunction,
                 crossover: Crossover,
                 selection: Selection,
                 mutation: Mutation,
                 left_boundary: float,
                 right_boundary: float,
                 dimensions: int,
                 chromosome_count: int,
                 chromosome_size: int,
                 epochs_amount: int,
                 elite_chromosome_count: int,
                 crossover_rate: float,
                 mutation_rate: float,
                 inversion_rate: float,
                 selection_count: int,
                 maximization: bool):
        self.fitness_function = fitness_function
        self.crossover = crossover
        self.selection = selection
        self.mutation = mutation

        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.dimensions = dimensions

        self.chromosome_count = chromosome_count
        self.chromosome_size = chromosome_size

        self.epochs_amount = epochs_amount
        self.elite_chromosome_count = elite_chromosome_count

        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.inversion_rate = inversion_rate
        self.selection_count = selection_count
        self.maximization = maximization
