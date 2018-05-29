input_f = input("Enter an input file name:")
output_f = input("Enter an output file name:")
this_line = 0

outfile = open(output_f, 'w')

with open(input_f, 'r') as infile:
    for line in infile.readlines():
        this_line += 1
        outfile.write('/* ' + str(this_line) + ' */ ' + line +'\n')

infile.closed
outfile.closed