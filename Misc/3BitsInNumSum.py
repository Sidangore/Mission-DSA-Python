mod = 1000000007

def count_ones(num):
    count = 0
    while num:
        count += (num & 1)
        num >>= 1
    return count


sum = 0
n = 7
for i in range(1, n + 1):
    if count_ones(i) == 3:
        sum = (sum + i) % mod

print(sum)