import pandas as pd
import matplotlib
matplotlib.use("QT4Agg")
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)

import statsmodels.api as sm


from data import *

ts_=pd.read_csv(tsfile,parse_dates=[0])
ts = ts_.set_index("Date")
tsm_ = ts.groupby(ts.index.year).apply(lambda grp: grp.nlargest(NMAXVALS,"Value").mean())
tsm = pd.DataFrame(dict(Date=tsm_.index, Value=tsm_.Value))
# save the data
tsm.to_csv(resfile)
ax=sns.regplot(x=tsm.Date,y=tsm.Value, ci=CI)
ax.set(xlabel=XLAB, ylabel=YLAB)
if NMAXVALS>1:
    t="Station {}. Mean of annual largest {} values.\nLinear regression with {}% confidence bands."
else:
    t="Station {}. Annual maximum values.\nLinear regression with {}% confidence bands."
t=t.format(STATION, NMAXVALS, CI)
ax.set_title(t)
plt.show()