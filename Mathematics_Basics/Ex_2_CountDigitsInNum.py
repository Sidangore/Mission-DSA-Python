x = int(input("Enter x: "))
if x == 0:
    print("No. of Digits = ", 1)
    exit(0)
count = 0
while x != 0:
    x = x // 10
    count += 1
print("No. of Digits = ", count)