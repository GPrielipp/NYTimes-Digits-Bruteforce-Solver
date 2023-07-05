# read the data
filedata = []
with open('winningmove.txt', 'r') as fd:
    filedata = fd.read().split("[option]\n")

# remove any empty arrays
def clean(arr):
    out = []
    for el in arr:
        if el != "":
            out.append(el)
    return out

# find the best
best = None
linecounts = 10 # max could be 6 or 7 (don't feel like counting)
for option in filedata:
    lines = clean(option.split("\n"))
    if len(lines) < linecounts and len(lines) > 0:
        best = lines
        linecounts = len(lines)

# print the best
print('\n'.join(best[::-1]))