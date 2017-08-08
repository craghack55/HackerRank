import math

AB = float(raw_input())
BC = float(raw_input())

result = math.degrees(math.atan(AB / BC))
result = int(round(result, 0))

print str(result) + "°"