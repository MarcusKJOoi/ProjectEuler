import math


def is_prime(a_number):
    prime = True
    for smaller_number in range(2, a_number):
        if not (a_number % smaller_number):
            prime = False
    return prime


if __name__ == '__main__':
    number = 600851475143
    number_squared = math.trunc(math.sqrt(number))
    for i in range(number_squared, 0, -1):
        rem = number % i
        if rem == 0:
            if is_prime(i):
                print(i)
