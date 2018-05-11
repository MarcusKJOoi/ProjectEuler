def divisible(a_number, num_list):
    for num in num_list:
        if a_number % num != 0:
            return False
    return True


if __name__ == '__main__':

    numbers = [i for i in range(20, 10, -1)]

    found = False
    smallest_number = 2520
    while not found:
        smallest_number += 20
        if divisible(smallest_number, numbers):
            found = True
    print(smallest_number)
