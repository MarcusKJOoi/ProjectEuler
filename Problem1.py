total_sum = 0

for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += 1

print(total_sum)
