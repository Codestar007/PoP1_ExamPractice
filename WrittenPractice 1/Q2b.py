def search (s, slst, size):
    for elm in range(size):
        if s == slst[elm]:
            return slst[elm + 1]
    return -1

myFile  = open("thefile.txt", "r")
nameList = myFile.readline().strip().split(" ")
myFile.close()
prompt = "Enter a name: "
name = ""
while(name != "XXX"):
    name = input(prompt)
    if name != "XXX":
        print("Grade:", search(name, nameList,len(nameList)))
print("Good bye.")

