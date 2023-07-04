# doesn't save the correct length of characters to print

linecounts = 10 # max could be 6 or 7 (don't feel like counting)
numbytes = 0
start = None
end = None
with open('winningmove.txt', 'r') as fd:
    count = 0
    for line in fd.readlines():
        if line == '\n':
            start = fd.tell()
            if count < linecounts:
                linecounts = count
                end = fd.tell()
                savebytes = numbytes
            numbytes = 0
            count = 0
        else:
            numbytes += len(line)
            count += 1
    fd.seek(start)
    shortest = fd.read(end-start)
    print(shortest)