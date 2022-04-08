import math
li = list()
print(li)
li = []
print(li)
li = [1, 2, 3, 4, 5]
print(li)
li = list([1, 2, 3, 4, 5, 6, 7])
print(li)

li.append(11)
print(li)
li[len(li):] = [22]
print(li)
li.extend([33])
print(li)
li += [1]  # li = li + [44]
print(li)
li.insert(0, 77)
print(li)

li.remove(1)
print(li)
# li.remove(0)
print(li.pop())
print(li)
print(li.pop(1))
print(li)
li.clear()
print(li)
del li[:]

li = list([44, 1, 2, 3, 4, -11, 5, 6, 7, 11, 22, 33])
# print(li.index(0))
print(li.index(1))
print(li.index(4, 2, 5))
print(li.count(0))
print(1 in li)
print(0 not in li)

print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

li.reverse()
print(li)

li1 = li.copy()
print(li1)
li1.append(-33)
print(li)
print(li1)
li2 = li[:]
print(li2)


def create(m, n):
    li = []
    for x in range(m, n+1):
        li.append(x)
    return li


print(create(1, 10))
print(list(map(lambda x: x, range(1, 11))))

# list comprehensions
print([x for x in range(1, 11)])
print([x**2 for x in range(1, 11)])
print([(x, y) for x in [1, 2, 3] for y in [3, 2, 5]])
print([(x, y) for x in [1, 2, 3] for y in [3, 2, 5] if x != y])

li = []
for x in [1, 2, 3]:
    for y in [3, 2, 5]:
        if x != y:
            li.append((x, y))
print(li)

print([(x, x**3) for x in range(1, 11)])
li = list([44, 1, 2, 3, 4, -11, 5, 6, 7, 11, 22, 33])
print([x for x in li if x >= 0])
print([abs(x) for x in li])

print(math.pi)
print([str(round(math.pi, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print([[row[i] for row in matrix] for i in range(3)])

trans = []
for i in range(3):
    trans_row = []
    for row in matrix:
        trans_row.append(row[i])
    trans.append(trans_row)
    print(trans_row)

print(trans)

print(li)
del li[2]
print(li)
del li[3:5]
print(li)
del li  # del li[:]
# print(li)

li = list([44, 1, 2, 3, 4, -11, 5, 6, 7, 11, 22, 33])
for i, v in enumerate(li):
    print('{0}=>{1}'.format(i, v))

for v in reversed(li):
    print('{0}'.format(v), end=' ')
print()

for i in sorted(set(li)):
    print(i, end=' ')
print()

print(li)
