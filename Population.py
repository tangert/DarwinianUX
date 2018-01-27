# Author: Tyler Angert
# Population class which represents a collection of button sequences

from Individual import Individual
from Globals import buttons
from Globals import GENE_LENGTH
import random

class Population(object):

    mutation_rate = 0

    population = []
    mating_pool = []
    target_sequence = []



    generations = 0
    fully_evolved = False

    perfect_fitness = 1

    def __init__(self, target_sequence, mutation_rate, pop_max):

        self.target_sequence = target_sequence
        self.mutation_rate = mutation_rate
        self.population = [0] * pop_max

        # Initialize the population with random individuals with the same length
        # as the target sequence

        for i in range (0, len(self.population)):
            self.population[i] = Individual(len(buttons))

        self.calc_fitness()

    # MARK: Basic genetic functions
    def calc_fitness(self):
        for i in range(0, len(self.population)):
            self.population[i].calc_fitness(self.target_sequence)


    def natural_selection(self):

        max_fitness = 0

        # See which Individual's fitness is the highest
        for i in range(0, len(self.population)):
            if(self.population[i].fitness > max_fitness):
                max_fitness = self.population[i].fitness

        self.mating_pool = [0] * len(self.population)

        for pop_i in range(0, len(self.population)):

            fitness = self.normalize(self.population[pop_i].fitness,
                                     0, max_fitness,
                                     0, 1)

            # fitness = float(self.population[pop_i].fitness)

            #gives certain elements a higher prevelance in the next
            #mating pool based on its fitness
            multiplier = int(fitness * len(self.population))

            for mate_i in range(0, multiplier):
                self.mating_pool[mate_i] = self.population[pop_i]


    def generate(self):

        for i in range(0, len(self.population)):

            a = random.randint(0, len(self.mating_pool)-1)
            b = random.randint(0, len(self.mating_pool)-1)

            partner_a = self.mating_pool[a]
            partner_b = self.mating_pool[b]

            child = partner_a.crossover(partner_b, 10)
            child.mutate(self.mutation_rate)

            self.population[i] = child

        self.generations += 1

    #converts a given value into another range
    def normalize(self, value, initial_start, initial_end, final_start, final_end):
        return final_start + (final_end - final_start) * \
                             ((value - initial_start) / (initial_end - initial_start))

    # MARK: Convenience functions
    def get_fittest_individual(self):

        record = 0
        index = 0

        for i in range(0, GENE_LENGTH):
            if self.population[i].fitness > record:
                record = self.population[i].fitness
                index = i

        if record == self.perfect_fitness:
            self.fully_evolved = True

        return self.population[index]

    def get_worst_individual(self):

        # initialize to be an impossibly high fitness
        record = 2
        index = 0

        for i in range(0, GENE_LENGTH):
            if self.population[i].fitness < record:
                record = self.population[i].fitness
                index = i

        return self.population[index]