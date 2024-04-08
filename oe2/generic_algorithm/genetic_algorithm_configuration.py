from dataclasses import dataclass

from oe2.generic_algorithm.crossovers.crossover import Crossover
from oe2.generic_algorithm.fitnessfunctions.fitness_function import FitnessFunction
from oe2.generic_algorithm.mutations.mutations import Mutation
from oe2.generic_algorithm.selections.selection import Selection


@dataclass
class GeneticAlgorithmConfiguration:
    fitness_function: FitnessFunction
    crossover: Crossover
    selection: Selection
    mutation: Mutation

    left_boundary: float = -20
    right_boundary: float = 20
    dimensions: int = 2

    chromosome_count: int = 200
    chromosome_size: int = 10

    epochs_amount: int = 100
    elite_chromosome_count: int = int(0.05 * chromosome_count)

    crossover_rate: float = 0.7
    mutation_rate: float = 0.3
    inversion_rate: float = 0.2
    selection_count: int = 40
