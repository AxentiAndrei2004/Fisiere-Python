with open ('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    c=int(a)*2 
    d= int(b)*3
if int(a)<int(b):
    c=int(b)*2
    d=int(a)*3
with open ('produs.txt', 'w') as f:
    f.write(str(c))
    f.write('\n')
    f.write(str(d))