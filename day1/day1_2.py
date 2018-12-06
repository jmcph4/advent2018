total = 0
states = set()
states.add(0)

while True:
    for line in open("input.txt", "r").readlines():
        total += int(line)

        if total not in states:
            states.add(total)
        else:
            print(total)
            exit(0)
