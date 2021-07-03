my_list = [1, 2, 5, 34, 6, 7]
my_list.insert(2, 3)
print(my_list)

list_1 = ['mukund', 'ebby']
list_2 = ['kevin', 'jasmine']

big_list = list_1 + list_2
print(big_list)


numbers = [5, 7, 21, 1, 0, -123, 0, 2]
words = ['bravo', 'xray', 'zulu', 'whiskey', 'oscar', 'sierra']

sorted_numbers = sorted(numbers, reverse=True)
sorted_words = sorted(words)

print(sorted_numbers)
print(sorted_words)

s1 = 'hello,'
s2 = ' world!'
s3 = s1 + s2

print(s3)

s = 'hello! '
print(s * 100)

s = 'to be or not to be'
words = s.split(' ')
sorted_words = sorted(words)
print(sorted_words)

list_of_strings = ['toobie', 'aurnought', 'toobie']
big_string = ' '.join(list_of_strings)
print(big_string)
l_o_s = big_string.split(' ')
print(l_o_s)

string_number = '42'
print(float(string_number) * 2)

number = int(input('type your number: '))

# f(x) = x + 5

# -----
# | 9 |  
# |   |
# -----

# -------------
# |    x      |
# |           |
# |    f      |
# -------------

def triple_my_number(number):
    tripled_number = number * 3
    return tripled_number

def quadruple_my_number(number):
    quad_number = number * 4
    return quad_number

def sum_and_divide(numbers, divisor):
    if divisor == 0:
        return None
    count = 0
    for number in numbers:
        count += number

    result = count / divisor
    return result


number = 4
tripled_number = triple_my_number(number)
quad_number = quadruple_my_number(number)
print(tripled_number)
print(quad_number)

nums = [1,2,3,4,5]
answer = sum_and_divide(nums, 3)
print(answer)