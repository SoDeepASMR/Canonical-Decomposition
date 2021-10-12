import sys

vertical_line = ' │ '
i = int(sys.argv[1])
orig_i = i

number = 2
while True:
    if i == number:
        print(int(i), ' '*(len(str(orig_i)) - len(str(i))), vertical_line, number, sep='')
        break
    elif i % number == 0:
        print(int(i), ' '*(len(str(orig_i)) - len(str(i))), vertical_line, number, sep='')
        i = i // number
        number = 2
        continue

    number += 1
