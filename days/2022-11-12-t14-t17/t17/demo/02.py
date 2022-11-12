f = open("17.txt")
sm = 0
while True:
    line = f.readline()
    if not line:
        break
    sm += int(line)
print(sm)
