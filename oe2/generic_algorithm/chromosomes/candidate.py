from dataclasses import dataclass
from typing import List

from oe2.generic_algorithm.chromosomes.chromosome import Chromosome, generate_chromosomes


@dataclass
class Candidate:
    chromosomes: List[Chromosome]


def generate_candidates(dimensions: int, count: int, chromosome_size: int, left_boundary: float, right_boundary: float) -> List[Candidate]:
    return [Candidate(generate_chromosomes(dimensions, chromosome_size, left_boundary, right_boundary))  for _ in range(count)]


