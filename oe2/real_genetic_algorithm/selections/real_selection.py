from typing import List


from real_genetic_algorithm.chromosomes.real_candidates import RealCandidates


class RealSelection:
    def select(self, population: RealCandidates, num_select: int, fitness_function: str):
        pass


class RealBestSelection(RealSelection):
    pass

    

class RealRouletteWheelSelection(RealSelection):
    pass
   

class RealTournamentSelection(RealSelection):
    pass

    