# This program uses a Genetic Algorithm to find the best values to maximize the (arbitrary) function,
#
#                           -4a + 2b + (-3.5)c + (-5)d + 11e + (-4.7)f
#
# Where a, b, c, d, e, and f are values randomly initialized and then improved on by the algorithm.
#
# Credits to Ahmed Gad for providing the outline of the program in
# https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6

# Hyperparameters

# Population (and children) size. - Comment out to use default value of 8
sol_per_pop = 8

# Number of parents to take genes from for children. - Comment out to use default value of 3
num_parents = 3

# Number of generations to run for. - Comment out to use default value of 20
num_generations = 20

# Inputs of the equation. - Feel free to mess with these as well! If you do, note that the function you will be
# calculating will be different.
equation_inputs = [-4, 2, -3.5, -5, 11, -4.7]

# If desired, set a deterministic seed value - Use None if you want it to be random.
seed_value = None

# Start of Code

import numpy as np

def cal_pop_fitness(equation_inputs, pop):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function caulcuates the sum of products between each input and its corresponding weights
    fitness = np.sum([gene * equation_inputs[index] for index, gene in enumerate(pop)])
    return fitness

def select_mating_pool(pop, fitness, num_parents=3):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parentInd = np.argsort(fitness)[-num_parents:][::-1].tolist()
    parents = []
    for i in parentInd:
        parents.append(pop[i])
    return parents

def crossover(parents, offspring_size=8):
    Totoffspring = []
    for offspring in range(offspring_size):
        os = []
        for index in range(len(parents[0])):
            parentInd = np.random.choice(len(parents))
            parent = parents[parentInd]
            os.append(parent[index])
        Totoffspring.append(np.asarray(os))
    return np.asarray(Totoffspring)

def mutation(offspring_crossover):
    offspring = []
    for offsp in offspring_crossover:
        if np.random.random() > .5:
            index = np.random.choice(len(offsp))
            offsp[index] = np.random.uniform(low=-4, high=4)
        offspring.append(offsp)
    return offspring

np.random.seed(seed_value)

pop_size = (sol_per_pop, len(equation_inputs))

offspring_size = sol_per_pop

# Creating the initial population.
new_population = np.random.uniform(low=-4.0, high=4.0, size=pop_size)

generation = 0
while generation != num_generations: # Could add a fitness stop condition as well.
    fitness = []
    for pop in new_population:
        fitness.append(cal_pop_fitness(equation_inputs, pop))
    if generation % 5 == 0:
        print("\n", f"Fitness at Generation {generation}:", np.max(fitness))
        print(" Pop. Values :", new_population[np.argmax(fitness)])

    parents = select_mating_pool(new_population, fitness, num_parents=num_parents)
    children = crossover(parents, offspring_size=offspring_size)
    children = mutation(children)
    new_population = children
    generation += 1

print("\n", f"End Fitness (Generation: {generation}):", np.max(fitness))
print(" End Pop. Values :", new_population[np.argmax(fitness)])
print(" Equation Inputs :", equation_inputs, "\n")