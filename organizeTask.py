#! usr/bin/python3
import pandas as pd
import numpy as np 
DefchunkSize=1000
filenamebase="F:\\rawdata\\batch_task"
filetype=".csv"
ckiter=0
header_batch_task=["task_name", "instance_num", "job_name","task_type", "status", "start_time", "end_time", "plan_cpu","plan_mem"]
header_machine_meta=["machine_id","time_stamp ", "failure_domain_1","failure_domain_2","cpu_num","mem_size","status"]
taskraw=pd.read_csv(filenamebase+filetype,header=None , chunksize=DefchunkSize,names=header_batch_task)
for chunk in taskraw:
    chunk.to_csv(filenamebase+str(ckiter)+filetype,index=False)
    ckiter=ckiter+1
print("finish")




