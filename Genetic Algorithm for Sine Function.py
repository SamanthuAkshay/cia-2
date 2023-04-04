import random
import math


def sine_function(x, amplitude, frequency, phase):
    return amplitude * math.sin(frequency * x + phase)

def find_maximum_sine_value(lower_limit, upper_limit, population_size, num_generations, mutation_rate):
    # Define the chromosomes
    def create_chromosome():
        amplitude = random.uniform(0, 1)
        frequency = random.uniform(0, 1)
        phase = random.uniform(0, math.pi)
        return [amplitude, frequency, phase]
    

    def fitness(chromosome):
        max_value = -math.inf
        for x in range(lower_limit, upper_limit + 1):
            y = sine_function(x, chromosome[0], chromosome[1], chromosome[2])
            if y > max_value:
                max_value = y
        return max_value
    
    
    population = [create_chromosome() for i in range(population_size)]
    
    for generation in range(num_generations):
        # Evaluate the fitness of each chromosome
        fitness_values = [fitness(chromosome) for chromosome in population]
        
     
        def selection(fitness_values):
            sum_fitness = sum(fitness_values)
            probabilities = [fitness_value / sum_fitness for fitness_value in fitness_values]
            return random.choices(population, probabilities, k=2)
        
        def crossover(parents):
            offspring = [0, 0, 0]
            for i in range(3):
                offspring[i] = (parents[0][i] + parents[1][i]) / 2
            return offspring
        
        def mutation(chromosome):
            for i in range(3):
                if random.random() < mutation_rate:
                    chromosome[i] = random.uniform(0, 1) if i < 2 else random.uniform(0, math.pi)
            return chromosome
        
        offspring = []
        for i in range(population_size):
            parents = selection(fitness_values)
            child = crossover(parents)
            child = mutation(child)
            offspring.append(child)
        

        offspring_fitness_values = [fitness(chromosome) for chromosome in offspring]
        

        combined_population = population + offspring
        combined_fitness_values = fitness_values + offspring_fitness_values
        population = [combined_population[i] for i in random.choices(range(len(combined_population)), combined_fitness_values, k=population_size)]
    

    fitness_values = [fitness(chromosome) for chromosome in population]
    max_fitness_index = fitness_values.index(max(fitness_values))
    return population[max_fitness_index], max(fitness_values)

lower_limit = 0
upper_limit = 10
population_size = 20
num_generations = 50
mutation_rate = 0.1

best_chromosome, max_fitness_value = find_maximum_sine_value(lower_limit, upper_limit, population_size, num_generations, mutation_rate)

print("Best chromosome:", best_chromosome)
print("Maximum fitness value:", max_fitness_value)
