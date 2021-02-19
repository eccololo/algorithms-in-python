import brutal_force_search
import utilities

min_list_range = 1
max_list_range = 10000
min_item_range = 1
max_item_range = 101
searched_number = 101

random_list = utilities.create_random_shuffles_list(max_list_range, min_list_range, max_item_range, min_item_range)

number_of_searches = brutal_force_search.brutal_search(random_list, searched_number)
print(f"Brutal search searched {searched_number} number {number_of_searches} times.")