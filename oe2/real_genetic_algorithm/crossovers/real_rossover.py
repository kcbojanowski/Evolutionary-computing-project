
from abc import abstractmethod, ABC
from typing import List
from real_genetic_algorithm.chromosomes.real_candidates import RealCandidates
from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome


class RealCrossover(ABC):
    @abstractmethod
    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> List[RealChromosome]:
        if len(chromosome1.real_representation) != len(chromosome2.real_representation):
            raise ValueError("N")
        return None

    def crossover_candidates(self, first_candidate: RealCandidates, second_candidate: RealCandidates) -> RealCandidates:
        crossed_chromosomes = []
        for i in range(len(first_candidate.chromosomes)):
            children = self.crossover(first_candidate.chromosomes[i], second_candidate.chromosomes[i])
            crossed_chromosomes.append(children[0])
            crossed_chromosomes.append(children[1])
        return RealCandidates(crossed_chromosomes)