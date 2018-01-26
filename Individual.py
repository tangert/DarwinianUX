# Author: Tyler Angert
# Individual class which represents a particular sequence of button combinations

import random
from Constants import buttons

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

        print "genes: {}".format(self.genes)


    def calc_fitness(self, target):
        #calculate a score for each given sequence of buttons
        score = 0

        #go through and check if the given sequence matches the target sequence
        #dont need to check if theyre equal
        #just need to check if the buttons are the same
        #remove duplicates from set


        #grab the unique items in the genes
        # turn into its own array

        gene_set = set(self.genes)
        target_set = set(target)
        common_set = target_set.intersection(gene_set)
        score = len(common_set)

        self.difference = len(target_set) - len(common_set)
        self.fitness = score / len(target_set)

    def get_sequence(self):
        return self.genes

    def crossover(self, partner):

        #new child button sequence
        child = Individual(len(self.genes))
        midpoint = random.randint(0, len(self.genes))

        for i in range (0, len(self.genes)):
            if (i > midpoint):
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        return child

    def mutate(self, mutation_rate):

        for i in range( 0, len(self.genes) ):

            probability = random.uniform(0,1)

            if ( probability < mutation_rate ):
                self.genes[i] = random.choice(buttons)