import random


# Creates random shuffled list from min to max elements number with min to max elements
def create_random_shuffles_list(max_list, min_list, max_item, min_item):
    random_list = []
    for n in range(min_list, max_list):
        number = random.randint(min_item, max_item)
        random_list.append(number)

    return random_list


# Print execution time of some intruction or function.
def print_execution_time(start, stop, text):
    text += " execution time:"
    print(text, "{0:.8f}s,".format(stop - start))
