from real_genetic_algorithm.chromosomes.real_chromosome import RealChromosome

class CenterOfGravityCrossover:
    def crossover(self, chromosome1: RealChromosome, chromosome2: RealChromosome, fitness_function: str) -> RealChromosome:
        dimension = len(chromosome1.real_representation)
        new_genes = [(chromosome1.real_representation[i] + chromosome2.real_representation[i]) / 2 for i in range(dimension)]
        return [RealChromosome(new_genes, fitness_function)]

