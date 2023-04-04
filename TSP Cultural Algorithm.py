import numpy as np
import random

# Define the TSP problem as a matrix of distances between cities
distances = np.array([[0, 10, 15, 20],
                      [10, 0, 35, 25],
                      [15, 35, 0, 30],
                      [20, 25, 30, 0]])

# Define the population size, the number of generations, and the knowledge transfer rate
pop_size = 50
num_generations = 100
knowledge_transfer_rate = 0.2

# Define the cultural knowledge as a list of city indices
cultural_knowledge = [0, 1, 2, 3]

# Define the function to calculate the total tour length
def tour_length(tour, distances):
    return sum([distances[tour[i], tour[i+1]] for i in range(len(tour)-1)]) + distances[tour[-1], tour[0]]

# Define the function to generate a random tour
def generate_tour(num_cities):
    return random.sample(range(num_cities), num_cities)

# Initialize the population as a list of random tours
population = [generate_tour(distances.shape[0]) for _ in range(pop_size)]

# Evaluate the initial population
fitness = [tour_length(tour, distances) for tour in population]

# Iterate over generations
for generation in range(num_generations):
    # Sort the population by fitness
    sorted_indices = np.argsort(fitness)
    population = [population[i] for i in sorted_indices]
    fitness = [fitness[i] for i in sorted_indices]

    # Select the best solutions as elites
    elites = population[:int(pop_size * knowledge_transfer_rate)]

    # Update the cultural knowledge with the elites
    cultural_knowledge = list(set(cultural_knowledge) | set(elites[0]))

    # Generate new solutions using cultural knowledge
    new_population = []
    while len(new_population) < pop_size:
        # Generate a new solution by combining cultural knowledge with random mutations
        new_solution = random.sample(cultural_knowledge, len(cultural_knowledge))
        for i in range(len(new_solution)):
            if random.random() < 0.1:
                # Apply a random mutation with probability 0.1
                j = random.randrange(len(new_solution))
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_population.append(new_solution)

    # Evaluate the new population
    new_fitness = [tour_length(tour, distances) for tour in new_population]

    # Replace the population with the new population
    population = elites + new_population[len(elites):]
    fitness = fitness[:len(elites)] + new_fitness[len(elites):]

# Print the best tour and its length
best_tour = population[0]
best_length = fitness[0]
print('Best tour:', best_tour)
print('Best length:', best_length)
