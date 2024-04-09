from abc import abstractmethod, ABC

from genetic_algorithm.chromosomes.candidate import Candidate
from genetic_algorithm.chromosomes.chromosome import Chromosome


class Crossover(ABC):
    @abstractmethod
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        if len(chromosome1.binary_representation) != len(chromosome2.binary_representation):
            raise ValueError("N")
        return None

    def crossover_candidates(self, first_candidate: Candidate, second_candidate: Candidate) -> Candidate:
        crossed_chromosomes = []
        for i in range(len(first_candidate.chromosomes)):
            crossed_chromosomes.append(self.crossover(first_candidate.chromosomes[i], second_candidate.chromosomes[i]))
        return Candidate(crossed_chromosomes)
