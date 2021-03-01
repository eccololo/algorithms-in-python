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


# This is welcome text message function. Prints welcome message.
def print_welcome():
    print("********************************************")
    print("* Welcome to Algorithms in Python Program. *")
    print("********************************************")
    print("* I wrote this program to learn more about various algorithms implemented in Python.")
    print("* I post it on Github because I am looking for an opportunity to work in IT industry as an intern.")
    print("* I am interested in working with Python Language and Django Framework.")
    print("* If you have any job opportunity for me you can contact me through my blog www.mstem.net and "
          "social media platforms like Linkedin.com.")
    print("*" * 30)


# This function prints konsole menu for this program
def print_main_menu():
    print("************************************")
    print("* Main Menu: ")
    print("* 1 - Search Algorithms.")
    print("* 2 - Sorting Algorithms.")
    print("* 3 - Brutal Force Algorithms.")
    print("* 4 - Computational Complexity of Algorithms.")
    print("* W - Print Welcome Message.")
    print("* Q - Quit.")