from dataclasses import dataclass

from oe2.generic_algorithm.crossovers.crossover import Crossover
from oe2.generic_algorithm.fitnessfunctions.fitness_function import FitnessFunction
from oe2.generic_algorithm.selections.selection import Selection


@dataclass
class GeneticAlgorithmConfiguration:
    fitness_function: FitnessFunction
    crossover: Crossover
    selection: Selection

    epochs_amount: int = 100
    elite_chromosome_count: int = 2
    chromosome_count: int = 20
    chromosome_size: int = 10
    left_boundary: int = -10
    right_boundary: int = -10
    crossover_rate: float = 0.7
    selection_count: int = 10
    dimensions = 2
