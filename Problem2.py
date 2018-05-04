first = 0
second = 1
next_num = 0
total_sum = 0

while first < 4000000:
    next_num = first + second
    first = second
    second = next_num

    if next_num % 2 == 0:
        total_sum += next_num

print(total_sum)
