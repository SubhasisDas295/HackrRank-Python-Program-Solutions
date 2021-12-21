import math
AB=int(input())
BC=int(input())
AC=math.sqrt((AB**2)+(BC**2))
MC=AC/2.0
Adj=BC/2.0
out=str(int(round(math.degrees(math.acos(Adj/MC)))))
print(out+chr(176))