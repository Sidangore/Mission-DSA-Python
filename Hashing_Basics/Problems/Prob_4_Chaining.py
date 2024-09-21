def separateChaining(hashSize, arr, sizeOfArray):
    hash_table = [[] for _ in range(hashSize)]
    for value in arr:
        index = value % hashSize
        if value not in hash_table[index]:
            hash_table[index].append(value)
    print(hash_table)
    return hash_table


if __name__ == '__main__':
    arr = [92, 4, 14, 24, 44, 91]
    sizeOfArray = len(arr)
    hashSize = 10

    separateChaining(hashSize, arr, sizeOfArray)
