from dataclasses import dataclass
from typing import List

from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome, generate_real_chromosomes


@dataclass
class RealCandidates:
    chromosomes: List[RealChromosome]


def generate_candidates(population_size: int, dimensions: int, left_boundary: float, right_boundary: float, fitness_function: str) -> RealCandidates:
    return RealCandidates(generate_real_chromosomes(population_size, dimensions, left_boundary, right_boundary, fitness_function))