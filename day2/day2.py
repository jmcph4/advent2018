def string2bag(s):
    d = {}

    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    return d

def checksum(strings):
    num_doubles = 0
    num_triples = 0

    # traverse list of strings
    for s in strings:
        counts = string2bag(s) # get (char, int) mapping

        # check for double-repeats
        if 2 in list(counts.values()):
            num_doubles += 1

        # check for triple-repeats
        if 3 in list(counts.values()):
            num_triples += 1

    return num_doubles * num_triples

print(checksum(line.strip() for line in open("input.txt", "r").readlines()))
