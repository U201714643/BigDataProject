import sys

curJob = None
curStart = 0
curEnd = 0
while True:
    try:
        line = sys.stdin.readline().strip()
        job, start, end = line.split()
        try:
            start = int(start)
            end = int(end)
        except ValueError:
            continue
        if curJob == job:
            curStart = min(curStart, start)
            curEnd = max(curEnd, end)
        else:
            if curStart:
                print("{}   {}".format(curJob, curEnd-curStart))
            curJob = job
            curStart = start
            curEnd = end
    except:
        break
if(curJob):
    print("{}   {}".format(curJob, curEnd-curStart))
