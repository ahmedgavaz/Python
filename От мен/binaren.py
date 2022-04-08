binary_file=open("binary_file.bin",mode="wb+")
text="This is good"
encoded=text.encode("utf-8")
binary_file.write(encoded)
binary_file.seek(0)
binary_data=binary_file.read()
text=binary_data.decode("utf-8")
print("Text:",text)
for byte in binary_data:
    print(byte)
binary_file.close()   

