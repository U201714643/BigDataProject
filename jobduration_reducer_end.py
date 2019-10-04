import sys

curJob=None
curTime=0
while True:
    try:
        line=sys.stdin.readline().strip()
        job,time=line.split()
        try:
            time=int(time)
            except ValueError:
                continue
            if curJob==job:
                curTime=max(curTime, time) # max for end time
            else:
                if curTime:
                    print("{}   {}".format(curJob, curTime))
                curJob=job
                curTime=time
            except:
                break
        if(curJob==job):
            print("{}   {}".format(curJob, curTime))



