import time
from datetime import datetime
def time_to_unixtime(time_str):
    time_list=time_str.split(maxsplit=5)
    time_list += [0]*(9-len(time_list))
    t=tuple(map(int,time_list))
    local_time = int(time.mktime(t))
    print("Местное время:", local_time)
# seconds = time.time()
# print("Секунды с начала эпохи =", seconds)
# seconds = 1701324545.9450624
# local_time = time.ctime(seconds)
# print("Местное время:", local_time)
