with open ('input.txt', 'r') as f:
    a=f.readline()
with open ('output.txt', 'w') as f:
    f.write(str(int(a)-2))
    f.write ('\n')
    f.write(str(int(a)-1))
    f.write ('\n')
    f.write(str(int(a)))
    f.write ('\n')
    f.write(str(int(a)+1))
    f.write ('\n')
    f.write(str(int(a)+2))
    f.write ('\n')