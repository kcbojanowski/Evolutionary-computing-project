from genetic_algorithm.chromosomes.candidate import Candidate


class FitnessFunction:
    def compute(self, candidate: Candidate):
        raise NotImplementedError("Subclasses must implement this method")