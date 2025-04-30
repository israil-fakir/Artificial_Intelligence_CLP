import random

class Individual:
    def __init__(self, n):
        self.n = n
        self.genes = [random.randint(0, n - 1) for _ in range(n)]
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        non_attacking = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.genes[i] != self.genes[j] and abs(self.genes[i] - self.genes[j]) != abs(i - j):
                    non_attacking += 1
        return non_attacking

    def mutate(self):
        idx1, idx2 = random.sample(range(self.n), 2)
        self.genes[idx1], self.genes[idx2] = self.genes[idx2], self.genes[idx1]


class Population:
    def __init__(self, size, n):
        self.n = n
        self.individuals = [Individual(n) for _ in range(size)]
        self.size = size
        self.max_fitness = (n * (n - 1)) // 2
        self.fittest = self.get_fittest()

    def get_fittest(self):
        return max(self.individuals, key=lambda ind: ind.fitness)

    def select_parents(self):
        sorted_individuals = sorted(self.individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_individuals[0], sorted_individuals[1]

    def evolve(self):
        parent1, parent2 = self.select_parents()
        crossover_point = random.randint(1, self.n - 2)

        child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child = Individual(self.n)
        child.genes = child_genes
        child.fitness = child.calc_fitness()

        if random.random() < 0.3:
            child.mutate()
            child.fitness = child.calc_fitness()

        least_fit = min(self.individuals, key=lambda ind: ind.fitness)
        self.individuals[self.individuals.index(least_fit)] = child
        self.fittest = self.get_fittest()


def print_board(genes):
    n = len(genes)
    print("\nFinal Board (1 = Queen, 0 = Empty):")
    for row in range(n):
        line = ['0'] * n
        line[genes[row]] = '1'
        print(' '.join(line))


def solve_n_queens(n, population_size=100, max_generations=1000):
    pop = Population(population_size, n)
    generation = 0

    print(f"Target fitness: {(n * (n - 1)) // 2}")

    while pop.fittest.fitness < pop.max_fitness and generation < max_generations:
        generation += 1
        pop.evolve()
        print(f"Generation {generation}: Fitness = {pop.fittest.fitness}")

    if pop.fittest.fitness == pop.max_fitness:
        print("\n✅ Solution found!")
    else:
        print("\n⚠️ Max generations reached. Best solution:")

    print(f"Generation: {generation}")
    print("Genes (queen positions):", pop.fittest.genes)
    print_board(pop.fittest.genes)
    return pop.fittest.genes


# Run the algorithm
if __name__ == "__main__":
    n = 8  # You can change to any value >= 4
    solve_n_queens(n)
