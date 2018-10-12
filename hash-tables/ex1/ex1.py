def get_indices_of_item_weights(weights, limit):
    # set tuple
    pair = ()
    # build our hash table
    hashTable = {}

    for i, v in enumerate(weights):
        difference = limit - v
        # have we found this difference already?
        if (check_valid(hashTable, difference)):
            # sweet, return in proper order
            if (hashTable[difference] > i):
                pair = (hashTable[difference], i)
            else:
                pair = (i, hashTable[difference])
        # nope, add to the hash table
        hashTable[v] = i

    return pair


def check_valid(hashtable, key):
    try:
        hashtable[key]
        return True
    except:
        return False


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
