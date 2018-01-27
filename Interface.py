# Author: Tyler Angert
# Simulate the interface by finding the correct interface

from Population import Population

def init(target_sequence):
    mutation_rate = 0.01
    popmax = 100
    population = Population(target_sequence, mutation_rate, popmax)
    return population

def evolve(population):

    #First naturally select in order to form the mating pool
    population.natural_selection()
    population.generate()
    population.calc_fitness()

    #Checks the fittest individual and updates the record each time
    population.get_fittest_individual()

    if population.fully_evolved:
        print population.get_fittest_individual().genes
        print "total generations: {}".format(population.generations)

if __name__ == '__main__':
    #Initialize with a target sequence
    population = init([1,1,1,2,0])

    #Keep evolving until the best match is found
    while not population.fully_evolved:
        evolve(population)

