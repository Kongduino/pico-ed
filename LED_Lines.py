import board, time, random
from picoed import display
random.seed(time.monotonic_ns())

def hLine(x, y, w, i):
  lastPixel = x + w
  if lastPixel > 17:
      lastPixel = 17
  for px in range(x, lastPixel):
      display.pixel(px, y, i)

def vLine(x, y, h, i):
  lastPixel = y + h
  if lastPixel > 7:
      lastPixel = 7
  for py in range(y, lastPixel):
      display.pixel(x, py, i)

def diagLine(x, y, h, i):
  lastPixel = y + h
  if lastPixel > 7:
      lastPixel = 7
  for py in range(y, lastPixel):
      display.pixel(x, py, i)
      x += 1

display.clear()
display.scroll("Horizontal Lines")
time.sleep(.5)
for y in range(0, 7):
    if y>0:
        hLine(0, y-1, 17, 1)
    if y>1:
        hLine(0, y-2, 17, 0)
    hLine(0, y, 17, 12)
    if y<6:
        hLine(0, y+1, 17, 1)
    time.sleep(.1)

display.clear()
display.scroll("Vertical Lines")
time.sleep(.5)
for x in range(0, 17):
    vLine(x-1, 0, 7, 1)
    vLine(x-2, 0, 7, 0)
    vLine(x, 0, 7, 12)
    vLine(x+1, 0, 7, 1)
    time.sleep(.1)
display.clear()

display.clear()
display.scroll("Diagonals")
time.sleep(.5)
for x in range(-7, 17):
    diagLine(x-2, 0, 7, 0)
    diagLine(x-1, 0, 7, 1)
    diagLine(x, 0, 7, 12)
    diagLine(x+1, 0, 7, 1)
    time.sleep(.1)

display.clear()
display.scroll("56 random points")
time.sleep(.5)
points = []
while len(points)<56:
    points.append([random.randint(0, 17), random.randint(0, 7), random.randint(3, 20)])

for x in points:
    display.pixel(x[0], x[1], x[2])
    time.sleep(.1)
time.sleep(.5)
for x in points:
    display.pixel(x[0], x[1], 0)
time.sleep(.2)
for x in points:
    display.pixel(x[0], x[1], x[2])
time.sleep(.5)
for x in points:
    display.pixel(x[0], x[1], 0)
    time.sleep(.1)
