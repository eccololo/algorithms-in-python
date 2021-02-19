import brutal_force_search
import utilities
import random

min_list_range = 1
max_list_range = 10000
min_item = 1
max_item = 101
searched_number = 101

utilities.create_random_shuffles_list(max_list_range, min_list_range, max_item, min_item)

number_of_searches = brutal_force_search.brutal_search(random_list, searched_number)
print(f"Brutal search searched {searched_number} number {number_of_searches} times.")