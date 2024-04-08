def elite_strategy(population, num_select):
    """
    Split chromosomes to chosen ones and the rest of them

    Args:
    - population
    - num_select: Number of chromosomes or percentage if use_percentage=True.
    - use_percentage: Defines if num_select is number of percentage

    Returns:
    - Tuple with selected chromosomes and the rests of them
    """

    sorted_population = sorted(population, key=lambda chromosome: chromosome.fitness, reverse=True)
    selected = sorted_population[:num_select]
    remaining = sorted_population[num_select:]

    return selected, remaining
