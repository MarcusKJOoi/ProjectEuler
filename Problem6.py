def sum_square(num_list):
    temp = list(num_list)
    for num in range(len(temp)):
        temp[num] = temp[num] ** 2
    return sum(temp)


def square_sum(num_list):
    return sum(num_list) * sum(num_list)


if __name__ == '__main__':

    numbers = [i for i in range(1, 101)]
    sum_square(numbers)
    print(square_sum(numbers) - sum_square(numbers))
