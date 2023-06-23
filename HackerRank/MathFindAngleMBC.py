# Enter your code here. Read input from STDIN. Print output to STDOUT

# import
import math

# read input
AB = int(input()) # alias edge C
BC = int(input()) # alias edge A

# calculate hypotenus AC
AC = math.sqrt((AB**2 + BC**2)) # alias edge B

# calculate angle C using sin Law (A / sin a = B / sin b = C / sin c)
sinC = math.sin(math.radians(90)) / AC * AB
radC = math.asin(sinC)

### subtriangle BMC
MC = AC / 2
# calculate BM
BM = (BC**2 + MC**2) - (2*BC*MC*(math.cos(radC)))
BM = math.sqrt(BM)

# calculate angle B of triangle BMC
sinB = sinC / BM * MC
degreeB = math.degrees(math.asin(sinB))

# print result
print(f'{round(degreeB)}{chr(176)}')
