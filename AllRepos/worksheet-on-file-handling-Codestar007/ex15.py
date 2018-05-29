def defineKey(cryptkey):
    """generate key and return it as a string"""
    alphabeths = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rawKey = set(cryptkey)
    newkey = ""
    
    for L in range(len(cryptkey)):
        if newkey.find(cryptkey[L]) == -1:
            newkey = newkey + cryptkey[L]
    alphabeths.difference_update(rawKey)
    reverseAlpha = (''.join(sorted(''.join(str(i) for i in alphabeths), reverse=True)))  
    cryptcode = newkey + reverseAlpha
    return cryptcode

def createkeyMap(crypt_action, cryptkey):
    """generate cryting key MAP and return it as a dictionary"""
    alphabeths = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if crypt_action == "-e":  # encrypt
        cryptDict = dict(zip(alphabeths, cryptkey))
    elif crypt_action == "-d":  # decrypt
        cryptDict = dict(zip(cryptkey, alphabeths))
    return cryptDict

def encrypt_or_decrypt_file(input_f, output_f, cryptdict):
    """encrypts or decrypts a file"""
    outfile = open(output_f, 'w')
    cyptedText = ""

    with open(input_f, 'r') as infile:
        for line in infile.readlines():
            for ltr in line:
                try:
                    val = cryptdict[ltr]
                    cyptedText = cyptedText + val
                except KeyError:
                    print(ltr, "is not in the crpypto dictionary")
                    cyptedText = cyptedText + r"" + ltr + ""
            outfile.write(cyptedText)
    infile.close()
    outfile.close()
    return cyptedText

def main():
    """ Number of arguments: 4 arguments.
    Argument List: ['ex15.py', '-k<encrytionkey>', 'inputfile', 'outputfile']
    """

    import sys

    if len(sys.argv[1:]) < 4 or sys.argv[2][0:2] != '-k' or (sys.argv[1] != '-d' and sys.argv[1] != '-e'):
        print('Error: Nnumber of arguments: 4 required, ' + str(len(sys.argv)-1) + ' supplied.' 
        + '\nUsage: [ex15.py -e or -d  -k<encrytionkey>  <inputfile>  <outputfile>]')
        exit()
    else:
        #1. analyse arguments decide crypto action
        crypt_action, ckey, input_f, output_f = sys.argv[1:]
        cryptkey = ckey[2:len(ckey)]  # remove the '-k'
        #2. generate crypto key
        get_cryptKey = defineKey(cryptkey)
        #3. generate crpto map
        get_crptMap = createkeyMap(crypt_action, get_cryptKey)
        #4. encrypt or decrypt file
        encrypt_or_decrypt_file(input_f, output_f, get_crptMap)
        pass

# TESTS
#assert defineKey("FEATHER") == "FEATHRZYXWVUSQPONMLKJIGDCB"
mydict_e = {
    'A': 'F', 'B': 'E', 'C': 'A', 'D': 'T', 'E': 'H', 'F': 'R',
    'G': 'Z', 'H': 'Y', 'I': 'X', 'J': 'W', 'K': 'V', 'L': 'U',
    'M': 'S', 'N': 'Q', 'O': 'P', 'P': 'O', 'Q': 'N', 'R': 'M',
    'S': 'L', 'T': 'K', 'U': 'J', 'V': 'I', 'W': 'G', 'X': 'D',
    'Y': 'C', 'Z': 'B'
}

mydict_d = {
    'F': 'A', 'E': 'B', 'A': 'C', 'T': 'D', 'H': 'E',
    'R': 'F', 'Z': 'G', 'Y': 'H', 'X': 'I', 'W': 'J', 'V': 'K',
    'U': 'L', 'S': 'M', 'Q': 'N', 'P': 'O', 'O': 'P', 'N': 'Q',
    'M': 'R', 'L': 'S', 'K': 'T', 'J': 'U', 'I': 'V', 'G': 'W',
    'D': 'X', 'C': 'Y', 'B': 'Z'
}

#main()
#assert createkeyMap("-e", "FEATHRZYXWVUSQPONMLKJIGDCB") == mydict_e
#assert createkeyMap("-d", "FEATHRZYXWVUSQPONMLKJIGDCB") == mydict_d
#assert encrypt_file("inputfile.txt", "ouputfile.txt", mydict_e) == "YFOOCEXMKYTFC"
#assert encrypt_or_decrypt_file("inputfile_e.txt", "ouputfile_e.txt", mydict_e) == "YFOOC EXMKYTFC"
assert encrypt_or_decrypt_file("inputfile_d.txt", "ouputfile_d.txt", mydict_d) == "WHAT IS GOING ON HERE?"