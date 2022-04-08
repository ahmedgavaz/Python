dic = {}
print(dic)
dic = dict()

print(dic)
dic = {'ivan': '123-123', 'petyr': '111-222'}
print(dic)

dic['lili'] = '444-333'
print(dic)

dic['petyr'] = '656-566'
print(dic)

del dic['ivan']
print(dic)
# del dic['ivan']
print('ivan' in dic)

print(list(dic))
print(sorted(dic))

dic = dict([('ivan', '123-123'), ('petyr', '656-566'), ('maria', '111-222')])
print(dic)

dic = dict(ivan='123-123', petyr='656-566')
print(dic)

# dict comprehensions
print({x: x*2 for x in (1, 2, 3)})
print({x: x*2 for x in range(1, 11)})

dic = dict([('ivan', '123-123'), ('petyr', '656-566'), ('maria', '111-222')])
for k, v in dic.items():
    print(f'{k}=>{v}')
