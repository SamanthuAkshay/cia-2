import random
import numpy as np
class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.edges = np.zeros((num_nodes, num_nodes))
    
    def add_edge(self, i, j, distance):
        self.edges[i][j] = distance
        self.edges[j][i] = distance
class Ant:
    def __init__(self, start_node):
        self.start_node = start_node
        self.path = [start_node]
        self.visited_nodes = set([start_node])
        self.distance_travelled = 0
    
    def move_to_next_node(self, probabilities):
        next_node = random.choices(range(len(probabilities)), probabilities)[0]
        self.path.append(next_node)
        self.visited_nodes.add(next_node)
        self.distance_travelled += graph.edges[self.path[-2]][next_node]
    
    def can_move_to_node(self, node):
        return node not in self.visited_nodes

def find_shortest_path_in_graph(graph, num_ants, evaporation_rate, alpha, beta, num_iterations):
    pheromone_trails = np.ones((graph.num_nodes, graph.num_nodes))
    np.fill_diagonal(pheromone_trails, 0)
    
    for iteration in range(num_iterations):
        # Generate ants and let them move through the graph
        ants = [Ant(i) for i in range(graph.num_nodes)]
        for ant in ants:
            for i in range(graph.num_nodes - 1):
                current_node = ant.path[-1]
                unvisited_nodes = [node for node in range(graph.num_nodes) if ant.can_move_to_node(node)]
                if not unvisited_nodes:
                    break
                pheromone_values = np.power(pheromone_trails[current_node][unvisited_nodes], alpha)
                distance_values = np.power(1 / graph.edges[current_node][unvisited_nodes], beta)
                probabilities = pheromone_values * distance_values / np.sum(pheromone_values * distance_values)
                ant.move_to_next_node(probabilities)
            ant.distance_travelled += graph.edges[ant.path[-1]][ant.start_node]
        
        pheromone_trails *= (1 - evaporation_rate)
        for ant in ants:
            for i in range(graph.num_nodes - 1):
                pheromone_trails[ant.path[i]][ant.path[i+1]] += 1 / ant.distance_travelled
            pheromone_trails[ant.path[-1]][ant.start_node] += 1 / ant.distance_travelled
    shortest_path = None
    shortest_distance = np.inf
    for ant in ants:
        if ant.distance_travelled < shortest_distance:
            shortest_path = ant.path
            shortest_distance = ant.distance_travelled
    
    return shortest_path, shortest_distance
