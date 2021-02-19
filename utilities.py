import random


def create_random_shuffles_list(max_list, min_list, max_item, min_item):
    random_list = []
    for n in range(min_list, max_list):
        number = random.randint(min_item, max_item)
        random_list.append(number)

    return random_list
