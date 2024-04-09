from genetic_algorithm.crossovers.single_point_crossover import SinglePointCrossover
from genetic_algorithm.crossovers.three_point_crossover import ThreePointCrossover
from genetic_algorithm.crossovers.two_point_crossover import TwoPointCrossover
from genetic_algorithm.crossovers.uniform_crossover import UniformCrossover
from genetic_algorithm.fitnessfunctions.ackley import AckleyFunction
from genetic_algorithm.fitnessfunctions.martin_and_gaddy import MartinAndGaddyFunction
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm.genetic_algorithm_configuration import GeneticAlgorithmConfiguration
from genetic_algorithm.mutations.mutations import OnePointMutation, TwoPointMutation, BoundaryMutation
from genetic_algorithm.selections.roulette_wheel_selection import RouletteWheelSelection
from genetic_algorithm.selections.tournament_selection import TournamentSelection

configuration = GeneticAlgorithmConfiguration(
    AckleyFunction(),
    TwoPointCrossover(),
    TournamentSelection(2),
    TwoPointMutation()
)

genetic_algorithm = GeneticAlgorithm(configuration)
genetic_algorithm.perform()

