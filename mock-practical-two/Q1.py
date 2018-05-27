def search (str, lst, size):
    for i in range(size):
        if str == lst[i]:
            return i
    return -1

print(search ("me", ["hello","please", "give", "me","a","call"], 6))