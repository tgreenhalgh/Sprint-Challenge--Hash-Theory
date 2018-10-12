def reconstruct_trip(tickets):
    # build our hashtable
    hashTable = {}
    for key in tickets:
        if (key[0] == None):
            hashTable["start"] = key[1]
        elif key[1] == None:
            hashTable[key[0]] = "end"
        else:
            hashTable[key[0]] = key[1]

    # start our trip list
    trip = []
    if check_valid(hashTable, "start"):
        dest = hashTable["start"]
        trip.append(dest)
    else:
        return []

    while (check_valid(hashTable, dest) and dest != "end"):
        dest = hashTable[dest]
        # we done yet?
        if (dest == "end"):
            return trip
        #  keep on keeping on
        trip.append(dest)
    # not a complete trip, so return empty list
    return []


def check_valid(hashtable, key):
    try:
        hashtable[key]
        return True
    except:
        return False


if __name__ == '__main__':
    pass
