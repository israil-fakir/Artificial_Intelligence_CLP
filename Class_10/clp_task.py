import random


def get_fitness(ind):
    return ind.fitness

def get_fitness_index(i, individuals):
    return individuals[i].fitness

 
class Individual:
    def __init__(self, k, T):
        self.k = k
        self.T = T
        ft = [random.randint(0, 9) for _ in range(min(2, k))]
        self.genes = ft + [0] * (k - len(ft))
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        return 18 - abs((self.genes[0] + self.genes[1]) - self.T) # max 18,min 0 
    

class Population:
    def __init__(self, size, k, T):
        self.size = size
        self.individuals = [Individual(k, T) for _ in range(size)]

    def calculate_fitness(self):
        for ind in self.individuals:
            ind.fitness = ind.calc_fitness()

    def get_fittest(self):
        return max(self.individuals, key=get_fitness)

    def get_second_fittest(self):
        sorted_inds = sorted(self.individuals, key=get_fitness, reverse=True)
        return sorted_inds[1]

    def get_least_fittest_index(self):
        return min(range(self.size),
                   key=lambda i: get_fitness_index(i, self.individuals))


class GeneticAlgorithm:
    def __init__(self, T, k, pop_size=30, crossover_rate=0.8, mutation_rate=0.2):
        self.T, self.k = T, k
        self.pop = Population(pop_size, k, T)
        self.cr, self.mr = crossover_rate, mutation_rate
        self.generation = 0

    def selection(self):
        a, b = random.sample(self.pop.individuals, 2)
        return (a if get_fitness(a) >= get_fitness(b) else b,
                b if get_fitness(b) > get_fitness(a) else a)

    def crossover(self, p1, p2):
        if random.random() < self.cr and self.k > 1:
            pt = 1
            p1.genes[:pt], p2.genes[:pt] = p2.genes[:pt], p1.genes[:pt]

    def mutate(self, ind):
        for i in range(min(2, self.k)):
            if random.random() < self.mr:
                ind.genes[i] = random.randint(0, 9)

    def evolve(self, max_gens=500):
        self.pop.calculate_fitness()
        while self.generation < max_gens:
            best = self.pop.get_fittest()
            if best.fitness == 18:
                break

            
            sorted_inds = sorted(self.pop.individuals, key=get_fitness, reverse=True)
            new_inds = sorted_inds[:2]

            while len(new_inds) < self.pop.size:
                p1, p2 = self.selection()
                c1 = Individual(self.k, self.T); c1.genes = p1.genes[:]
                c2 = Individual(self.k, self.T); c2.genes = p2.genes[:]
                self.crossover(c1, c2)
                self.mutate(c1); self.mutate(c2)
                c1.fitness = c1.calc_fitness()
                c2.fitness = c2.calc_fitness()
                new_inds += [c1, c2]

            self.pop.individuals = new_inds[:self.pop.size]
            self.pop.calculate_fitness()
            self.generation += 1

        return self.pop.get_fittest()

 
def main():
    T = int(input("T = "))
    k = int(input("k = "))
    ga = GeneticAlgorithm(T, k)
    sol = ga.evolve()
    print("Output:")
    print(" ".join(str(x) for x in sol.genes))

if __name__ == "__main__":
    main()
