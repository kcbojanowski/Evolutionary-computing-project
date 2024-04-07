import numpy as np

class SelectionMethod:

    def select(self, population, num_select):
        """
        Selects chromosomes from populaction

        Args:
        - population: list of chromosomes
        - num_select: Number of chromosomes to select

        Returns:
        - List of selected chromosomes
        """
        raise NotImplementedError("Implement select() method in subclass")

class RouletteWheelSelection(SelectionMethod):

    def select(self, population, num_select):
        total_fitness = sum(chromosome.fitness for chromosome in population)
        selection_probs = [chromosome.fitness / total_fitness for chromosome in population]
        selected_indices = np.random.choice(len(population), size=num_select, replace=False, p=selection_probs)
        return [population[i] for i in selected_indices]

class TournamentSelection(SelectionMethod):

    def select(self, population, num_select, tournament_size=3):
        selected = []
        for _ in range(num_select):
            tournament = np.random.choice(population, size=tournament_size, replace=False)
            winner = max(tournament, key=lambda chromosome: chromosome.fitness)
            selected.append(winner)
        return selected

class EliteStrategy(SelectionMethod):
    def select(self, population, num_select):
        """
        Elite strategy

        Args:
        - population
        - num_select

        Returns:
        - List of selected (elite) chromosomes
        """
        sorted_population = sorted(population, key=lambda chromosome: chromosome.fitness, reverse=True)
        return sorted_population[:num_select]

    def select_and_split(self, population, num_select, use_percentage=False):
        """
        Split chromosomes to chosen ones and the rest of them

        Args:
        - population
        - num_select: Number of chromosomes or percentage if use_percentage=True.
        - use_percentage: Defines if num_select is number of percentage

        Returns:
        - Tuple with selected chromosomes and the rests of them
        """
        if use_percentage:
            num_select = int(len(population) * num_select / 100)

        sorted_population = sorted(population, key=lambda chromosome: chromosome.fitness, reverse=True)
        selected = sorted_population[:num_select]
        remaining = sorted_population[num_select:]

        return selected, remaining