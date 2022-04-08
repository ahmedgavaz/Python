def fib(n=1000):
    ''' Prints a Fibonachi series '''
    result = []
    a, b = 0, 1
    while a < n:
        # print(a, end=' ')
        result.append(a)  # result += [a]  # result = result+[a]
        a, b = b, a+b
    # print()
    return result


def func(a, L=[]):
    L.append(a)
    return L


def funcNone(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def function(a, b, c):
    pass


def f(pos1, /, pos_key, *, key1):
    print(pos1, pos_key, key1)


def add(x):
    return lambda y, z: x-y+z


# fib(2000)
# fib(1000)
print(fib)
print(fib())
print(fib(100))

print(1, 10, 100, sep=';', end=' ')
print(11, 101, 1001, sep=';')

print(func(1))
print(func(2))
print(func(3))

print(funcNone(1))
print(funcNone(2))
print(funcNone(3))

function(2, 3, 4)
# function(12, b=5, 22)
function(12, b=5, c=22)
function(a=2, b=4, c=12)
# function(2, a=0)

f(2, 10, key1=7)
# f(pos1=22, pos_key=10, key1=7)
# f(22, 10, 77)
f(22, pos_key=10, key1=77)

print(add(3))
f1 = add(3)  # x=3
print(f1(7, 5))  # y=7, z=5
