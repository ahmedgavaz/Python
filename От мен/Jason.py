import json
list1=['Ahmed Gavaz','Aksinia Fidosova', 'Aleksandar Avdzhiev',
       'Antonia Koleva', 'Dimitar Chavdarov', 'Dimitar Rabadzhiev',
       'Edis Madanski', 'Gergana Atanasova', 'Hristo Garkov',
       'Ines Damyanovska','Ivan Bashtenski', 'Ivan Kamenov', 'Ivan Stefanov',
       'Lorensia Davidkova','Marina Dimovska', 'Martin Genchev', 'Melis Ibisheva' ,
       'Mladen Chulev','Plamen Petrov', 'Radoslav Zdravkov', 'Sara Stanoevska',
       'Shteryu Atanasov',"Simona Mihova", 'Teona Denchevska', 'Tsvetan Vatovski',
       'Valensia Davidkova']
list2=[100,101,102,103,104,105,106,107,108,109,110]
dict = {
  "name": "Ahme",
  "age": 19,
  "city": "Gotse Delchev"
}
x=json.dumps(list1)
y=json.dumps(list2)
z=json.dumps(dict)
print(x)
print(y)
print(z)

