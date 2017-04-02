#Version    Date            Author      Comment
#   0.1     02-APR-2017     Staid03     Initial_Alt
#
#Script Purpose: simple Fibonacci number generation up to *limit*

from time import gmtime , strftime

aTime = (strftime("%Y%m%d_%H%M%S", gmtime()))
outFile = open(("Fibonacci_Python_%s.txt" % (aTime)), "w")
limit = 10000
x = 0
y = 1
z = x + y

outFile.write(x + "\n")
outFile.write(y + "\n")

while (z < limit):
    z = x + y
    outFile.write(z + "\n")
    x = y
    y = z

outFile.close()

