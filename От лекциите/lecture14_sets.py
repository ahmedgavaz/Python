s = set()
print(s)
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)

print(3 in s)
print(3 not in s)

# set comprehensions
print({x for x in 'abracadabra'})
print({x for x in 'abracadabra' if x not in 'abc'})
