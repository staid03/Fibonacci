#Version    Date            Author      Comment
#   0.1     02-APR-2017     Staid03     Initial
#
#Script Purpose: simple Fibonacci number generation up to *limit*

from time import gmtime , strftime

aTime = (strftime("%Y%m%d_%H%M%S", gmtime()))
outFile = open(("Fibonacci_Python_%s.txt" % (aTime)), "w")

def main():
    limit = 10000
    x = 0
    y = 1
    z = 0
    fileAppend(str(x))
    fileAppend(str(y))
    while (z < limit):
        z = x + y
        fileAppend(str(z))
        x = y
        y = z
    outFile.close()

def fileAppend(e):
    outFile.write(e + "\n")

main()