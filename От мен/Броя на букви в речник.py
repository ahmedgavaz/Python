text=input("Enter text:")
dict={}
for i in range(len(text)):
    if text[i] in dict:
        dict[text[i]]+=1
    else:
        dict[text[i]]=1
print(dict)
