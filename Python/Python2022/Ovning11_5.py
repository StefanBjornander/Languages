from sys import argv

with  open(argv[1], 'r') as fin, open(argv[2], 'w') as fout:
    for rad in fin:
        if argv[3] in rad:
            fout.write(rad)
    fin.close()
    fout.close()
