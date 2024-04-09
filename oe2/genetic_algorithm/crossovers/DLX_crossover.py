import random

from oe2.genetic_algorithm.crossovers.crossover import Crossover
from oe2.genetic_algorithm.chromosomes.chromosome import Chromosome


class DLX(Crossover):
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        
        def DLX_f(A, B, length):
            C = []
            D = []
            for i in range(0, length):
                C.append(A[i])
                D.append(B[i])
            Cl1 = random.randint(0, length-1)
            Cl2 = random.randint(0, length-1)
            Dl1 = random.randint(0, length-1)
            Dl2 = random.randint(0, length-1)
            alpha = C[Cl1]
            beta = D[Dl1]
            C[Cl2] = beta
            D[Dl2] = alpha
            return C, D

        Crossover.crossover(self, chromosome1, chromosome2)
        length = len(chromosome1.binary_representation)
        A = chromosome1.binary_representation
        B = chromosome2.binary_representation
        C, D = DLX_f(A, B, length)
        return Chromosome(C, chromosome1.left_boundary, chromosome1.right_boundary)

