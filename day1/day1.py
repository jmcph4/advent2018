total = 0

for line in open("input.txt", "r").readlines():
    total += int(line)

print(total)
