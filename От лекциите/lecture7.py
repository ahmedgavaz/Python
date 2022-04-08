import collections
import random

random.seed(100)
print(random.random())
l = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(l)
print(l)
print(random.uniform(1, 5))
print(random.randint(1, 5))
print(random.randrange(1, 50, 3))

numbers = []
for x in range(10):
    numbers.append(random.randint(-10, 10))
print(numbers)

filtered_data = []
for x in numbers:
    if x % 2 != 0:
        filtered_data.append(x)
print(filtered_data)

l = [x for x in numbers if x % 2 == 0]
print(l)

print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'Python')
print()


def concatenation(*data, sep=' '):
    return sep.join(data)


print(concatenation('I', 'like', 'Python'))
print(concatenation('I', 'like', 'Python', sep='#'))
print(concatenation('I', 'like', 'Python', sep=','))

print(list(range(1, 5)))
arg = [1, 5]
print(list(range(*arg)))


def unpack(key1, key2, key3):
    print(key1, key2, key3)


d = {'key1': 'I', 'key2': 'like', 'key3': 'Python'}
unpack(**d)

print(20*'*')
# stack
# Last In, First Out => LIFO
stack = [1, 2, 3, 4, 5]
print(stack)
# Last In
stack.append(22)
print(stack)
# First Out
print(stack.pop())
print(stack)

# Queue
# First In, First Out -> FIFO
queue = collections.deque([1, 2, 3, 4, 5])
print(queue)
queue.append(33)
# First In
queue.appendleft(22)
print(queue)
# First Out
print(queue.pop())
print(queue)
print(queue.popleft())
print(queue)

queue = [1, 2, 3, 4, 5]
queue.insert(0, 22)
print(queue)
print(queue.pop())
print(queue)
