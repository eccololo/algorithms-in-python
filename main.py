import brutal_force_search
import utilities
import time
import math

min_list_range = 1
max_list_range = 10000
min_item_range = 1
max_item_range = 101
searched_number = 101

start_list_creation = time.time()
random_list = utilities.create_random_shuffles_list(max_list_range, min_list_range, max_item_range, min_item_range)
stop_list_creation = time.time()

start_bs = time.time()
number_of_searches = brutal_force_search.brutal_search(random_list, searched_number)
stop_bs = time.time()

print(f"Brutal search searched {searched_number} number {number_of_searches} times in shuffled list.")
print(f"List has {max_list_range} items from {min_item_range} to {max_item_range}.")
utilities.print_execution_time(start_list_creation, stop_list_creation, "List shuffle")
utilities.print_execution_time(start_bs, stop_bs, "Brutal force search")