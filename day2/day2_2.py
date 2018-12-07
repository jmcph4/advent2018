def distance(a, b):
    a_len = len(a)
    b_len = len(b)
    max_len = max(a_len, b_len)
    min_len = min(a_len, b_len)

    dist = max_len - min_len

    for i in range(min_len):
        if a[i] != b[i]:
            dist += 1

    return dist

def differing_chars(a, b):
    a_len = len(a)
    b_len = len(b)
    max_len = max(a_len, b_len)
    min_len = min(a_len, b_len)

    diff = []

    for i in range(min_len):
        if a[i] != b[i]:
            diff.append(a[i])

    return diff


def shared_chars(a, b):
    difference = differing_chars(a, b)

    res = list(a)

    for char in difference:
        res.remove(char)

    return res

lines = [l.strip() for l in open("input.txt", "r").readlines()]

for line in lines:
    for other_line in lines:
        if distance(line, other_line) == 1:
            print("".join(shared_chars(line, other_line)))
            exit(0)
