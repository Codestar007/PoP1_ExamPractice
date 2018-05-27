def search (s, slst, size):
    for elm in range(size):
        if s == slst[elm]:
            return elm #slst[elm + 1]
    return -1

myFile  = open("thefile.txt", "r")
nameList = myFile.readline().strip().split(" ")
myFile.close()
prompt = "Enter a name: "
name = ""
while(name != "XXX"):
    name = input(prompt)
    if name != "XXX":
        print("Grade:", nameList[search(name, nameList,len(nameList)) + 1])
print("Good bye.")

