import pandas as pd
import numpy as np 

filenamebase="F:\\rawdata\\batch_task0"
filetype=".csv"

chunks=pd.read_csv(filenamebase+filetype, iterator=True, header=0)
for chk in chunks:
    print(chk)

