myFile = open("hello.txt", 'w')
myFile.write("Hello, World!")
myFile.close()

myFile2 = open("hello.txt", 'r')
greetings = myFile2.readline()
print(greetings)
myFile2.close()