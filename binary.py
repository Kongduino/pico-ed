import board, time, random
from picoed import display

random.seed(time.monotonic_ns())
display.clear()

def showBin(n):
    px = 0
    b = 1
    while px<8:
        x = n & b
        print(f"bit {n} & {b} = {x}")
        b = b << 1
        if x>0:
            display.pixel((8-px)*2, 3, 12)
            display.pixel((8-px)*2-1, 3, 12)
            display.pixel((8-px)*2, 4, 12)
            display.pixel((8-px)*2-1, 4, 12)
        else:
            display.pixel((8-px)*2, 3, 1)
            display.pixel((8-px)*2-1, 3, 1)
            display.pixel((8-px)*2, 4, 1)
            display.pixel((8-px)*2-1, 4, 1)
        px += 1

myList=[128,64,32,16,8,4,2,1]
for i in range(0, 5):
    myList.append(random.randint(0, 255))
for n in myList:
    v ="  "+str(n)
    display.show(v[-3:], 32)
    time.sleep(2)
    display.clear()
    showBin(n)
    time.sleep(5)
    display.clear()
