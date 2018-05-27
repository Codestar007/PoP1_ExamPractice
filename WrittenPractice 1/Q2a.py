def search (s, slst, size):
    for elm in range(size):
        if s == slst[elm]:
            return elm
    return -1

print(search("of", ["convict", "the", "Man", "of", "fraud"],5))
