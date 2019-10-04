#! usr/bin/env python
# can be modified for other counting job
import sys
#input comes from STDIN (standard input)  , line from batch_task output 
while True:
    try:
        line=sys.stdin.readline().strip()
        status=line.split()[5]  # 5 因为输出时多了0列作为索引
        if status=="Failed" or status =="Running" or status=="Terminated":
            print('{}   {}'.format(status, 1))
    except:
        break