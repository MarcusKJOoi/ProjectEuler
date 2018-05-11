def is_prime(a_number, prime_list):
    for prime in prime_list:
        if a_number % prime == 0:
            return False
    return True


if __name__ == '__main__':

    primes = [2, 3, 5, 7, 11, 13]
    current_num = 13
    while len(primes) != 10001:
        current_num += 1
        if is_prime(current_num, primes):
            primes.append(current_num)
    print(primes[-1])