def brutal_search(myList, target):
    for i in range(len(myList)):
        if myList[i] == target:
            return i
    return -1
