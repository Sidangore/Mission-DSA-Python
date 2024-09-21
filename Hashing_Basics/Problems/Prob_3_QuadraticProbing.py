def QuadraticProbing(hash_table, hash_size, arr, N):
    size = 0
    for element in arr:
        i = 0
        index = get_quad_hash(element, i, hash_size)

        while True:
            if hash_table[index] == -1:
                hash_table[index] = element
                size += 1
                break
            elif hash_table[index] == element:
                break
            i += 1
            index = get_quad_hash(element, i, hash_size)
        if size == hash_size:
            break

    print(hash_table)
    return hash_table


def get_quad_hash(element, i, hash_size):
    return (element + i**2) % hash_size


if __name__ == '__main__':
    hash_size = 11
    hash_table = [-1 for _ in range(hash_size)]
    arr = [21, 10, 32, 43]
    N = len(arr)

    QuadraticProbing(hash_table, hash_size, arr, N)
