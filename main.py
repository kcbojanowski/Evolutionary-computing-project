from models.chromosome import generate_chromosomes
from crossover.single_point_crossover import SinglePointCrossover
from crossover.two_point_crossover import TwoPointCrossover
from crossover.three_point_crossover import ThreePointCrossover
from crossover.uniform_crossover import UniformCrossover

left, right = generate_chromosomes(2, 10, -5, 5)
single = SinglePointCrossover()
two = TwoPointCrossover()
three = ThreePointCrossover()
uniform = UniformCrossover()
print(left)
print(right)

print(uniform.crossover(left, right))

