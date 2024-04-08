from oe2.generic_algorithm.crossovers.single_point_crossover import SinglePointCrossover
from oe2.generic_algorithm.crossovers.three_point_crossover import ThreePointCrossover
from oe2.generic_algorithm.crossovers.two_point_crossover import TwoPointCrossover
from oe2.generic_algorithm.crossovers.uniform_crossover import UniformCrossover
from oe2.generic_algorithm.fitnessfunctions.ackley import AckleyFunction
from oe2.generic_algorithm.fitnessfunctions.martin_and_gaddy import MartinAndGaddyFunction
from oe2.generic_algorithm.genetic_algorithm import GeneticAlgorithm
from oe2.generic_algorithm.genetic_algorithm_configuration import GeneticAlgorithmConfiguration
from oe2.generic_algorithm.mutations.mutations import OnePointMutation, TwoPointMutation, BoundaryMutation
from oe2.generic_algorithm.selections.roulette_wheel_selection import RouletteWheelSelection
from oe2.generic_algorithm.selections.tournament_selection import TournamentSelection

configuration = GeneticAlgorithmConfiguration(
    AckleyFunction(),
    TwoPointCrossover(),
    TournamentSelection(2),
    TwoPointMutation()
)

genetic_algorithm = GeneticAlgorithm(configuration)
genetic_algorithm.perform()

