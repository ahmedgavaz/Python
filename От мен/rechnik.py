#syzdavane na rechnik
d=dict()
d1=dict(name='ivan', last_name='petrov')
d3=dict([ ('name', 'polina'), ('l_name', 'koleva')])
print(d3)
print(d1)

#zapylvane na rechnik element po element
d= { }
d['name'] = 'petyr'
d['last_name'] = 'kolev'
print(d)
d = {'name':'ivan', 'last_name': 'ivanov'}
print(d)

#operacii
d = {'name': 'ivan', 'last_name': 'ivanov'}
d['name']
#print(d[d['fname']) - greshka

#proverka za nalichie na kliuch chrez operator in
b = 'fname' in d
print(b) #false

#opredelqne na broq na kliuchovete v rechnika
len(d)
print(len(d))#2

#dobavqne na elementi v rechnika
d['s_name'] = 'petrov'
print(d)

#premahvane na elemnt ot rechnik - izpolzva se del
del d['s_name']
print(d)

#metodi keys() i value()
keys = list(d.keys())
keys.sort()
for key in keys:
    print("{0} => {1} ".format(key, d[key]), end=' ')
