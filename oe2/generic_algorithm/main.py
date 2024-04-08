# from oe2.generic_algorithm.crossovers.single_point_crossover import SinglePointCrossover
# from oe2.generic_algorithm.fitnessfunctions.martin_and_gaddy import MartinAndGaddyFunction
# from oe2.generic_algorithm.genetic_algorithm import GeneticAlgorithm
# from oe2.generic_algorithm.genetic_algorithm_configuration import GeneticAlgorithmConfiguration
# from oe2.generic_algorithm.selections.roulette_wheel_selection import RouletteWheelSelection
#
# configuration = GeneticAlgorithmConfiguration(
#     MartinAndGaddyFunction(),
#     SinglePointCrossover(),
#     RouletteWheelSelection()
# )
#
# genetic_algorithm = GeneticAlgorithm(configuration)
# genetic_algorithm.perform()
from oe2.generic_algorithm.chromosomes.candidate import generate_candidates

x = generate_candidates(2, 2, 3, -10, 10)
for i in x:
    print(i)
