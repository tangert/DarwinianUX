# Author: Tyler Angert
# Population class which represents a collection of button sequences

from Individual import Individual
from Constants import buttons
import random

class Population(object):

    mutation_rate = 0

    population = []
    mating_pool = []
    target_sequence = []

    generations = 0
    is_fully_evolved = False

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

        """
        Calculates fitness for each individual in a population
        """

        for i in range(0, len(self.population)):
            self.population[i].calc_fitness(self.target_sequence)


    def natural_selection(self):

        max_fitness = 0

        # See which Individual's fitness is the highest
        for i in range(0, len(self.population)):
            if(self.population[i].fitness > max_fitness):
                max_fitness = self.population[i].fitness

        # Add to mating pool
        for i in range(0, len(self.population)):

            fitness = self.normalize(self.population[i].fitness,
                                     0, max_fitness,
                                     0, 1)

            multiplier = fitness * 100

            for j in range(0, multiplier):
                self.mating_pool[j] = self.population[i]


    def generate(self):

        for i in range(0, len(self.population)):

            a,b = random.randrange(0, len(self.mating_pool))

            partner_a = self.mating_pool[a]
            partner_b = self.mating_pool[b]

            child = partner_a.crossover(partner_b)
            child.mutate(self.mutation_rate)

            self.population[i] = child

        self.generations+=1

    #converts a given value into another range
    def normalize(self, value, initial_start, initial_end, final_start, final_end):
        return final_start + (final_end - final_start) * \
                             ( (value - initial_start) / (initial_end - initial_start))

    # MARK: Convenience functions
    def get_fittest_individual(self):
        print "getting best"
        record = 0
        index = 0

        for i in range(0, len(self.population)):
            if self.population[i].fitness > record:
                record = self.population[i].fitness
                index = i

        if record == self.perfect_fitness:
            self.is_fully_evolved = True

        return self.population[index]


    def is_fully_evolved(self):
        return self.is_fully_evolved
