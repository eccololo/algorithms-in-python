# This is brutal force search function. Search for an element from begining to an end.
def brutal_search(myList, target):
    for i in range(len(myList)):
        if myList[i] == target:
            return i
    return -1
