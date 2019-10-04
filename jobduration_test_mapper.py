import pandas as pd
import numpy as np 

filenamebase="F:\\rawdata\\batch_task0" # 改为源数据时要改掉header
filetype=".csv"

chunks=pd.read_csv(filenamebase+filetype, iterator=True, header=0,index_col=None, chunksize=1)
for chk in chunks:                                         
   # print(chk)
   # print("{}".format(chk["job_name"])
   # print(chk.values)
    print("{}  {}  {}".format(chk.values[0][2],chk.values[0][5],chk.values[0][6]))

