filename = './Training/data.txt'

with open(filename, mode = 'r') as f:
    with open('out.txt', mode = 'a') as f_out:
        for line in f:
            line = line.rstrip('\n')
            name, grade = line.split()
            if int(grade) >= 7:
                print(name)
                print(name, file = f_out)
