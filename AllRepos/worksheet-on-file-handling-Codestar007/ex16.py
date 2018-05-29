#  Reference: code adapted from page 3, 4 Allen B. Downey, Files, 2017.

def walk(parentDir):
    import os
    import re
    cwd  = os.getcwd()
    myList = re.split(r"\\|\.|_", cwd)

    criteria = myList[-1]
    dirList = os.listdir(parentDir)

    for name in dirList:
        path = os.path.join(parentDir, name)

        if path.find(criteria) == -1:
            if os.path.isfile(path):
                print(path)
            else:
                walk(path)

walk('..')
