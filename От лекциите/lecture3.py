# print('hello')
# print("python")
# print("don't use it")
# print('don\'t use it')
# print("\"Yes\", she said")
# print('"Yes", she said')
# print("Hello\nPython\tWorld")
# print('C:\python\demos\names')
# print(r'C:\python\demos\names')
# print("""
# Usage something
# new
# as switch
# """)
# print("""\
# Usage something
# new
# as switch\
# """)
# print(3*'-'+'Python'+3*'-')

txt = 3*'-'+'Python'+3*'='
# print(txt)
# print(txt[0])
# print(txt[5])
# print(txt[-1])
# print(txt[-6])

# print(txt[0:3])
# print(txt[3:5])
# print(txt[3:])
# print(txt[:4])
# print(txt[:])

# print(txt[2:5]+txt[7:9])
# print(txt[-3:-1])
# # print(txt[33]) error!
# print(txt[3:33])
# print(txt[33:])

# # strings are immutable
# # txt[0] = '#'
# # txt[2:] = '##'

# txt1 = '#'+txt[3:]
# print(txt1)
# print(len(txt1))

txt2 = txt[3:]
print(txt2.capitalize())
# print(txt2.casefold())
print(txt2.center(20))
print(txt2.count('='))
print(txt2.endswith('n'))
print(txt2.find('yt'))

print('This is {0}'.format(txt2[0:-3]))

print(txt2.find('H'))
# print(txt2.index('H')) error

print(txt2.islower())
print(txt2.isupper())
print(txt2.lower())
print(txt2.upper())
print(txt2.lower().islower())
print(txt2.upper().isupper())
