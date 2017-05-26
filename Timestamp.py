#coding:utf-8

from pytz import timezone
from datetime import datetime

def writeTime(filename):
    now = datetime.now(timezone('UTC'))
    f = open(filename,'w')
    f.write(now.strftime('%Y-%m-%d %H:%M:%S'))
    f.close()

def readTime(filename):
    f = open(filename,'r')
    for row in f:
        dt=datetime.strptime(row,'%Y-%m-%d %H:%M:%S')
    f.close()
    return dt
