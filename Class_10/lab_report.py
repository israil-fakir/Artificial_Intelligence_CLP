import random

class Individual:
    def __init__(self):
        self.gene_length = 5
        self.genes = [random.randint(0, 1) for _ in range(self.gene_length)]
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        return sum(self.genes)

class Population:
    def __init__(self, size):
        self.size = size
        self.individuals = [Individual() for _ in range(size)]
        self.fittest = self.get_fittest()

    def get_fittest(self):
        return max(self.individuals, key=lambda ind: ind.fitness)

    def get_second_fittest(self):
        sorted_individuals = sorted(self.individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_individuals[1]

    def get_least_fittest_index(self):
        return min(range(self.size), key=lambda i: self.individuals[i].fitness)

    def calculate_fitness(self):
        for individual in self.individuals:
            individual.fitness = individual.calc_fitness()
        self.fittest = self.get_fittest()

class GeneticAlgorithm:
    def __init__(self, pop_size=10):
        self.population = Population(pop_size)
        self.fittest = None
        self.second_fittest = None
        self.generation_count = 0

    def selection(self):
        self.fittest = self.population.get_fittest()
        self.second_fittest = self.population.get_second_fittest()

    def crossover(self):
        crossover_point = random.randint(0, self.fittest.gene_length - 1)
        for i in range(crossover_point):
            self.fittest.genes[i], self.second_fittest.genes[i] = \
                self.second_fittest.genes[i], self.fittest.genes[i]

    def mutation(self):
        for individual in [self.fittest, self.second_fittest]:
            mutation_point = random.randint(0, individual.gene_length - 1)
            individual.genes[mutation_point] = 1 - individual.genes[mutation_point]

    def get_fittest_offspring(self):
        return self.fittest if self.fittest.fitness > self.second_fittest.fitness else self.second_fittest

    def add_fittest_offspring(self):
        self.fittest.fitness = self.fittest.calc_fitness()
        self.second_fittest.fitness = self.second_fittest.calc_fitness()
        index = self.population.get_least_fittest_index()
        self.population.individuals[index] = self.get_fittest_offspring()

    def run(self):
        self.population.calculate_fitness()
        print(f"Generation: {self.generation_count} Fittest: {self.population.fittest.fitness}")

        while self.population.fittest.fitness < 5:
            self.generation_count += 1
            self.selection()
            self.crossover()
            if random.randint(0, 6) < 5:
                self.mutation()
            self.add_fittest_offspring()
            self.population.calculate_fitness()
            print(f"Generation: {self.generation_count} Fittest: {self.population.fittest.fitness}")

        print(f"\nSolution found in generation {self.generation_count}")
        print(f"Fitness: {self.population.fittest.fitness}")
        print("Genes:", ''.join(map(str, self.population.fittest.genes)))

# Run the genetic algorithm
ga = GeneticAlgorithm()
ga.run()
