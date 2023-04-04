
import random

# Define the distance matrix between cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Define the size of the population and the number of generations to run
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000

# Define the mutation rate
MUTATION_RATE = 0.01

# Define the fitness function
def fitness(solution):
    total_distance = 0
    for i in range(len(solution)):
        j = (i + 1) % len(solution)
        total_distance += distances[solution[i]][solution[j]]
    return 1 / total_distance

# Define the crossover function
def crossover(parent1, parent2):
    child = [None] * len(parent1)
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start, len(parent1) - 1)
    for i in range(start, end + 1):
        child[i] = parent1[i]
    remaining = [x for x in parent2 if x not in child]
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining.pop(0)
    return child

# Define the mutation function
def mutate(solution):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, len(solution) - 1)
        j = random.randint(0, len(solution) - 1)
        solution[i], solution[j] = solution[j], solution[i]

# Initialize the population
population = []
for i in range(POPULATION_SIZE):
    solution = list(range(len(distances)))
    random.shuffle(solution)
    population.append(solution)

# Run the genetic algorithm
for generation in range(NUM_GENERATIONS):
    # Evaluate the fitness of each solution
    fitnesses = [fitness(solution) for solution in population]

    # Select the parents for the next generation
    parent1 = population[fitnesses.index(max(fitnesses))]
    parent2 = population[fitnesses.index(sorted(fitnesses)[-2])]

    # Create the next generation
    next_generation = [parent1, parent2]
    while len(next_generation) < POPULATION_SIZE:
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        child = crossover(parent1, parent2)
        mutate(child)
        next_generation.append(child)

    population = next_generation

# Print the best solution found
best_solution = max(population, key=fitness)
print(best_solution)
