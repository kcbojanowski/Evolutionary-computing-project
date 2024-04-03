from models.chromosome import generate_chromosomes


chromosomes = generate_chromosomes(10, 5, -5, 5)
for chromosome in chromosomes:
    print(chromosome)

