import random
from typing import List


class Chromosome:
    def __init__(self, binary_representation: List[int], left_boundary: int, right_boundary: int):
        self.binary_representation = binary_representation
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.value = self.decode_chromosome()

    def decode_chromosome(self):
        decimal_value = int(''.join([str(i) for i in self.binary_representation]), 2)
        return self.left_boundary + decimal_value * (self.right_boundary - self.left_boundary) / (
                    2 ** len(self.binary_representation) - 1)

    def __str__(self):
        return str(self.binary_representation)


def generate_chromosomes(count: int, chromosome_size: int, left_boundary: int, right_boundary: int) -> List[Chromosome]:
    return [Chromosome([random.randint(0, 1) for _ in range(chromosome_size)], left_boundary, right_boundary) for _ in
            range(count)]
