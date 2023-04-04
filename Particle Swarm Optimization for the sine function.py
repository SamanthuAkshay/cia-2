import random
import math

def sine_function(x, amplitude, frequency, phase):
    return amplitude * math.sin(frequency * x + phase)

def find_extreme_sine_values(lower_limit, upper_limit, swarm_size, num_iterations, w, c1, c2):
    
    def create_particle():
        amplitude = random.uniform(0, 1)
        frequency = random.uniform(0, 1)
        phase = random.uniform(0, math.pi)
        velocity = [random.uniform(-1, 1) for i in range(3)]
        return [amplitude, frequency, phase, velocity, amplitude, frequency, phase]
    
    def fitness(chromosome):
        max_value = -math.inf
        min_value = math.inf
        for x in range(lower_limit, upper_limit + 1):
            y = sine_function(x, chromosome[0], chromosome[1], chromosome[2])
            if y > max_value:
                max_value = y
                chromosome[4] = max_value
                chromosome[5] = chromosome[0]
                chromosome[6] = chromosome[1]
            if y < min_value:
                min_value = y
                chromosome[7] = min_value
                chromosome[8] = chromosome[0]
                chromosome[9] = chromosome[1]
        return max_value - min_value
    
    swarm = [create_particle() for i in range(swarm_size)]   
    global_best_particle = [0, 0, 0, [0, 0, 0], -math.inf, 0, 0, math.inf, 0, 0]
    for iteration in range(num_iterations):
        # Evaluate the fitness of each particle
        for particle in swarm:
            particle_fitness = fitness(particle)
            # Update the personal best for each particle
            if particle_fitness > particle[4] - particle[7]:
                particle[4] = particle_fitness + particle[7]
                particle[5] = particle[0]
                particle[6] = particle[1]
            if particle_fitness > global_best_particle[4] - global_best_particle[7]:
                global_best_particle = list(particle)
        for particle in swarm:
            for i in range(3):
                particle[3][i] = w * particle[3][i] + c1 * random.uniform(0, 1) * (particle[5+i] - particle[i]) + c2 * random.uniform(0, 1) * (global_best_particle[5+i] - particle[i])
                particle[i] += particle[3][i]
                # Ensure the values are within bounds
                if i < 2:
                    particle[i] = max(0, min(1, particle[i]))
                else:
                    particle[i] = max(0, min(math.pi, particle[i]))
        
    return (global_best_particle[5:8], global_best_particle[8:])
