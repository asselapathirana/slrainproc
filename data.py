import os
STATION="GLENCORSE"
file="glencorse.csv"
tsfile=os.path.splitext(file)[0]+"_ts.csv"
sty=1989
stm=10
skiplines=3
sep=";"
slash='/'
SM = 10 # october
TGYB = 25 # if two digits are < this then its 20xx, else 19xx.
HEADERS = 3
TOL = 0.01 # numerical tolerance 
NMAXVALS = 5 # how many values to average
CI = 95 # confidence interval %
XLAB = "Year"
YLAB = "Rainfall (mm)"