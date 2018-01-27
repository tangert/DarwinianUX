# Author: Tyler Angert
# Individual class which represents a particular sequence of button combinations

import random
from Globals import buttons
from Globals import GENE_LENGTH

class Individual(object):

    # Holds the sequence of button combinations
    genes = []
    fitness = 0
    difference = 0

    def __init__(self, length):

        # Initialize the genes array
        # according to how many buttons are passed in

        #on future generations, need to adjust length of genes based on buttons that get "evolved out"
        self.genes = [0] * length

        # Fill in the values
        for i in range(0, length):
            self.genes[i] = random.randint(0, length-1)

    def calc_fitness(self, target):

        #uses common elements since you are just trying to find the buttons that perform the functions
        gene_set = set(self.genes)
        target_set = set(target)
        common = target_set.intersection(gene_set)

        # fitness is the percentage of the common elements are a part of the whole set.
        self.fitness = float(len(common)) / len(gene_set)

    def get_sequence(self):
        return self.genes

    def crossover(self, partner, length):

        child = Individual(length)
        midpoint = random.randint(0, length)

        for i in range (0, length):
            if (i > midpoint):
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        return child

    def mutate(self, mutation_rate):
        for i in range(0, len(self.genes)):
            if random.uniform(0, 1) < mutation_rate:
                self.genes[i] = random.choice(buttons)