def is_palindrome(num):
    num_string = str(num)
    length = len(num_string)
    for index in range(length // 2):
        if num_string[index] != num_string[length - (index+1)]:
            return False
    return True


palindrome_list = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        product = i * j
        if is_palindrome(product):
            palindrome_list.append(product)

print(max(palindrome_list))
