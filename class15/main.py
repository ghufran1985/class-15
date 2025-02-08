fn = open('c.txt', 'r')

fn1 = open('d.txt', 'w')

cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
    else:
        pass

fn1.close()

fn1 = open('d.txt', 'r')

const1 = fn1.read()

print(const1)