"""
Name:  Kizito Jegede
ID: Codestar007
Course: MSc CS - PoP 1

Assignment Four: (Please refer to 'README.dm' for full specification)
Program Title: Travelling salesman problem
Program Description:    This program aims to solves a simplified version
                        of the travelling salesman problem. The salesman 
                        wishes to visit a number of "cities", only once, 
                        then return to their starting point (it doesn't 
                        matter what city is the starting point.). However, 
                        the salesman also wishes to minimise the total 
                        distance that must be traveled.

"""

import random
import math
import copy
from earth_distance import distance
import time
import sys
import datetime


def read_cities(file_name):
    """
    Reads in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
        [(state, city, latitude, longitude), ...] 
    """

    with open(file_name, "r") as stream:
        cities_list = [tuple(line.strip().split("\t")) for line in stream]
    return cities_list


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Only one or two digits after the decimal point of the location.
    """

    # Finds longest city name for use in formatting
    name_size = max(len(road_map[i][1]) for i in range(len(road_map)))

    # prints list
    for j in range(len(road_map)):
        offset = " " * (name_size - len(road_map[j][1]))
        latitude = "%0.2f" % float(road_map[j][2])
        longitude = "%0.2f" % float(road_map[j][3])
        print(road_map[j][1] + offset + "  " + latitude + "  " + longitude)


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`.
    """

    total_distance = 0
    for i in (range(len(road_map))):
        x1 = float(road_map[i][2])
        y1 = float(road_map[i][3])
        x2 = float(road_map[(i + 1) % len(road_map)][2])
        y2 = float(road_map[(i + 1) % len(road_map)][3])
        total_distance += distance(x1, y1, x2, y2)
    return total_distance


def swap_adjacent_cities(road_map, index):
    """
    Take the city at location `index` in the `road_map`, and the city at 
    location `index+1` (or at `0`, if `index` refers to the last element 
    in the list), swap their positions in the `road_map`, compute the 
    new total distance, and return the tuple :
        (new_road_map, new_total_distance)
    """

    # deepcopy to prevent change to road_map
    new_road_map = copy.deepcopy(road_map)
    # Handles possible reference to last element in the list
    nxt_index = ((index + 1) % len(road_map))

    # Swap adjacent_cities
    new_road_map[index], new_road_map[nxt_index] = new_road_map[nxt_index], new_road_map[index]
    new_total_distance = compute_total_distance(new_road_map)
    return new_road_map, new_total_distance


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple: 
        (new_road_map, new_total_distance)
    """

    # deepcopy to prevent change to road_map
    new_road_map = copy.deepcopy(road_map)

    # Handles possibility that `index1==index2`
    if index1 == index2:
        return road_map, compute_total_distance(road_map)
    else:
        new_road_map[index1], new_road_map[index2] = new_road_map[index2], new_road_map[index1]
        new_total_distance = compute_total_distance(new_road_map)
        return new_road_map, new_total_distance


def shortest_city_to_city_map(road_map):
    """A heuristic helper function. Given a roadmap, determines which map 
    has the shortest total distance by constructing calling 
    `next_nearest_cities` a new map based on particular starting 
    city and its next nearest city (repeated with a different 
    city as a starting point).
    Returns tuple: (new_road_map, new_total_distance) if the new 
    path is shorter than the original, else returns the original
    road map and distance.
    """

    new_road_map = copy.deepcopy(road_map)  # Initialize `new_road_map`
    new_total_distance = compute_total_distance(road_map)
    for city in range(len(road_map)):
        best_map_so_far, shortest_dist_so_far = next_nearest_cities(road_map, city)
        if shortest_dist_so_far < new_total_distance:
            new_road_map = best_map_so_far
            new_total_distance = shortest_dist_so_far
    return new_road_map, new_total_distance


def next_nearest_cities(road_map, city_index):
    """A heuristic helper function. given a roadmap, and a city index,
    orders the cities according to the next nearest city 
    from the starting city and subsequent cities (city A to B to C etc..).
    Returns the tuple: (new_road_map, total_distance).
    """

    new_road_map = []  # holds the new best roadmap so far
    cities_visited = []  # holds index of all cities visited
    cities_pending = [i for i in range(len(road_map))]  # index of all cities
    cities_visited.append(city_index)  # Add starting city
    cities_pending.remove(city_index)  # remove starting city
    new_road_map.append(road_map[city_index])  # Add the starting node (A)
    while len(cities_pending) != 0:  # loop until no more cities to connect
        min_distance = compute_total_distance(road_map)  # reset
        for i in range(len(cities_pending)):
            x1 = float(road_map[city_index][2])
            y1 = float(road_map[city_index][3])
            x2 = float(road_map[cities_pending[i]][2])
            y2 = float(road_map[cities_pending[i]][3])
            result = distance(x1, y1, x2, y2)

            if result < min_distance and cities_pending[i] not in cities_visited:
                min_distance = result
                nearest_city_so_far = cities_pending[i]
        city_index = nearest_city_so_far
        cities_visited.append(city_index)  # add visited city
        cities_pending.remove(city_index)  # remove visited city
        new_road_map.append(road_map[city_index])
    total_distance = compute_total_distance(new_road_map)
    return new_road_map, total_distance

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `swap_adjacent_cities`, 
    try `10000` swaps, and each time keep the best cycle found so far. 
    After `10000` swaps, return the best cycle found so far.
    """

    LIST_SIZE = int(len(road_map))  # Constant instance to improve on
    SWAP_LOOP_RANGE = 10000  # Swap loop constraint
    best_cycle_so_far = road_map
    current_distance = compute_total_distance(road_map)
    swap_option = ("swap_cities", "swap_adjacent_cities")
    # Call helper function to reduce raodmap based on greedy algo heuristics.
    brute_city_map, brute_distance = shortest_city_to_city_map(road_map)

    # The starting cycle distance, Select a random swap
    for i in range(SWAP_LOOP_RANGE):
        if i < LIST_SIZE and brute_distance < current_distance:  # 50 loops to swap cities by brute force
            # change road_map to match brute force map order
            index1 = i  # get the index
            index2 = best_cycle_so_far.index(brute_city_map[i])  # find index of same value in road_map
            new_map, new_distance = swap_cities(
                best_cycle_so_far, index1, index2)
            best_cycle_so_far = new_map  # save the new map
        else:
            select_option = int(len(swap_option) * random.random())
            if swap_option[select_option] == "swap_adjacent_cities":
                index1 = int(LIST_SIZE * random.random())
                index2 = int(LIST_SIZE * random.random())
                new_map, new_distance = swap_cities(
                    best_cycle_so_far, index1, index2)
            else:
                index = int(LIST_SIZE * random.random())
                new_map, new_distance = swap_adjacent_cities(
                    best_cycle_so_far, index)
            if new_distance < current_distance:
                best_cycle_so_far = new_map  # Assign new map
                current_distance = new_distance  # Assign new best distance

    return best_cycle_so_far

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """

    total_distance = compute_total_distance(road_map)
    cycle = ""
    for i in range(len(road_map)):
        x1 = float(road_map[i][2])
        y1 = float(road_map[i][3])
        x2 = float(road_map[(i + 1) % len(road_map)][2])
        y2 = float(road_map[(i + 1) % len(road_map)][3])

        dist_diff = "%0.2f" % distance(x1, y1, x2, y2)
        if (i + 1) % 5 == 0:
            add_new_line = "--> \n"  # adds linefeed
        else:
            add_new_line = ""
        #  Call function to construct string for this cycle
        cycle = (cycle + print_map_continue(road_map, i, dist_diff, add_new_line))

    print("\nBest Cycle:\n\n" + cycle + "\n\nTotal cost:" +
          str("%0.2f" % total_distance) + " Miles")

def print_map_continue(road_map, i, dist_diff, add_new_line):
    """
    Splits the `print_map` function. Given a road_map, distance between
    two cities, index number of city A, and a new line feed argument,
    works out the print string for the cycle, then returns the print string.
    """

    cycle = ""
    if i == 0:
        cycle = (cycle + road_map[((i + 1) % len(road_map))][1]
                 + " --(" + str(dist_diff) + "mi.)")
    elif i == len(road_map) - 1:  # last city in list
        cycle = (cycle + "--> " + road_map[((i + 1) % len(road_map))][1]
                 + " --(" + str(dist_diff) + "mi.)"
                 + " --> " + road_map[((i + 1) % len(road_map)) + 1][1])
    else:
        cycle = (cycle + "--> " + road_map[((i + 1) % len(road_map))][1]
                 + " --(" + str(dist_diff) + "mi.)" + add_new_line)

    return cycle

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """

    road_map = read_cities("city-data.txt")
    print_cities(road_map)
    best_cycle = find_best_cycle(road_map)
    print_map(best_cycle)

if __name__ == "__main__":
    main()


