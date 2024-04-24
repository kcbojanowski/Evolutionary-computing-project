import random
from typing import List


class RealChromosome:
    def __init__(self, real_representation: List[float], fitness_function: str):
        self.fitness_function = fitness_function
        self.real_representation = real_representation
        self.value = self.calculate_value()

    #TODO add fitness funciton and calculate value
    def calculate_value(self):
        value: float = 0
        match self.fitness_function:
            case 'martin-and-gady':
                pass #TODO return the real martin and gady function value for chromosome from some py package 
            case 'ackleys-function':
                pass #TODO return the real ackleys function value for chromosome from some py package  
        return value

    def __str__(self):
        return str(self.real_representation)

    def __repr__(self):
        return str(self.real_representation)


def generate_chromosome_values(left_boundary, right_boundary, chromosome_dimension):
    return [random.uniform(left_boundary, right_boundary) for _ in range(chromosome_dimension)]

def generate_real_chromosomes(population_size: int, chromosome_dimension: int, left_boundary: float, right_boundary: float, fitness_function: str) -> List[RealChromosome]:
    return [RealChromosome(generate_chromosome_values(left_boundary, right_boundary, chromosome_dimension), fitness_function) for _ in range(population_size)]
