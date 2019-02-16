import calendar
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)

with open("glencorse.csv") as df:
    raw = df.readlines()
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


raw=raw[HEADERS:]

def get_date(dd):
    mm = int(dd[2])
    y_ = [int(dd[0]), int(dd[1])]
    if mm < 12-SM+2: 
        mon = mm + SM-1
        yy = y_[0] 
    else:
        mon = mm - 12+SM-1
        yy = y_[1]
    if yy < TGYB: 
        yy = 2000+yy
    else:
        yy = 1900+yy    
    stdate = datetime.date(yy,mon,1)
    return stdate

dates=[]
values=[]
for i, lin in enumerate(raw):
    lin=lin.strip('\t\n '+sep)
    vals = lin.split(sep=sep)

    dd = vals[0].split(sep=slash)
    stdate = get_date(dd)
    # what is the last date:
    ldm = calendar.monthrange(stdate.year,stdate.month)[1]
    thesedays = [stdate+datetime.timedelta(days=x) for x in range(0,ldm)]
    thesevalues = [pd.to_numeric(x,errors='coerce') for x in vals[1:ldm+1]]
    check = pd.to_numeric(vals[-1],errors='coerce')
    if len(thesevalues) < len(thesedays):
        thesevalues=[np.nan for x in thesedays] # something wrong so fill with Nan
    dates += thesedays
    values += thesevalues
    if abs(sum(thesevalues)-check) > TOL: 
        print("Mismatch in last column sum {} vs {} at line {} starting like {}".format(sum(thesevalues), check, i, lin[:50]))
        
# now make a pandas series
pdates=[pd.Timestamp(x) for x in dates]
ts = pd.DataFrame(data={"Date":pdates,"Value":values})
ts=ts.set_index("Date")
tsm_ = ts.groupby(ts.index.year).apply(lambda grp: grp.nlargest(NMAXVALS,"Value").mean())
tsm = pd.DataFrame(dict(Date=tsm_.index, Value=tsm_.Value))
sns.regplot(x=tsm.Date,y=tsm.Value)
plt.show()
        
    
    
    