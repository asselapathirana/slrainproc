import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)

from data import *

ts_=pd.read_csv(tsfile,parse_dates=[0])
ts = ts_.set_index("Date")
tsm_ = ts.groupby(ts.index.year).apply(lambda grp: grp.nlargest(NMAXVALS,"Value").mean())
tsm = pd.DataFrame(dict(Date=tsm_.index, Value=tsm_.Value))
ax=sns.regplot(x=tsm.Date,y=tsm.Value, ci=CI)
ax.set(xlabel=XLAB, ylabel=YLAB)
plt.show()