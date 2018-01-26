# Author: Tyler Angert
# Simulate the interface by finding the correct interface

from Population import Population

#Global gene length variable that decreases with time
#as buttons are naturally selected
GENE_LENGTH = 0

def init(target_sequence, population):
    mutation_rate = 0.01
    popmax = 200
    population = Population(target_sequence, mutation_rate, popmax)

def evolve(population):
    population.natural_selection()
    population.generate()
    population.calc_fitness()

    if population.is_fully_evolved():
        print population.get_best_sequence()

if __name__ == '__main__':
    #Initialize with a target sequence
    population = Population([],0,0)

    init([0,3,4,5,2], population)

    #Keep evolving until the best match is found
    while not population.is_fully_evolved():
        evolve(population)
        print "evolving"