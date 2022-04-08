numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[1:3])
print(numbers[3:])
print(numbers[:4])
print(numbers[:])
print(numbers[-3:])
numbers += [11, 12, 13]  # numbers = numbers + [11,12,13]
print(numbers)
numbers[3] = 33
print(numbers)

text = 'hello pythons'
print(text)
# text[2] = 'H' error: str is immutable!
# print(text)

numbers.append(44)
print(numbers)
numbers[2:4] = [22, 33, 55, 66]
print(numbers)
numbers[2:4] = []
print(numbers)
numbers[:] = []
print(numbers)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = []
print(letters)

print(len(letters))

numbers = [[1, 2, 3], [4, 5, 6], ['a', 'b']]
print(numbers)
print(numbers[0][2])

# 0,1,1,2,3,5,8,13
a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a+b
    # temp = a
    # a = b
    # b = temp+b
print()

number = int(input('Number: '))
if number > 0:
    print('Number is greather than zero')
elif number == 0:
    print('Number is zero')
else:
    print('Number is less than zero')

if number >= 0 and number <= 10:
    print('Number in range [0,10]')

# a         b       a and b     a or b      not a
# false     false   false       false       true
# false     true    false       true
# true      false   false       true        false
# true      true    true        true

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

text = ['banana', 'lemon', 'orange', 'grape']
for word in text:
    print(word, len(word))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(numbers)
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 0:
        del numbers[i]
print(numbers)

odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)
