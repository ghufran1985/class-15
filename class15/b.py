file1 = open('a.txt ', 'r')
file2 = open('b.txt', 'w')

for line in file1.readlines():
    
    if not (line.startswith("Coding")):
        file2.write(line)

        print(line)

        file2.write(line)

file2.close()
file1.close()