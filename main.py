import brutal_force_search
import random

min = 1
max = 10000
searched_number = 101
random_list = []
for n in range(min, max):
    number = random.randint(1, 100000)
    random_list.append(number)
    
number_of_searches = brutal_force_search.brutal_search(random_list, searched_number)
print(f"Brutal search searched {searched_number} number {number_of_searches} times.")