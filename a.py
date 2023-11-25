# This is a sample Python script.
from collections import deque, defaultdict
import random
import time
from typing import List

import sys
import math

sys.stdout = open('test/output.txt', 'w')
sys.stdin = open('test/input.txt', 'r')

random.seed(time.time())
def helper():
    t = int(input())
    for i in range(10):
        count= 0
        x=0
        for _ in range(t):
            y = random.random()
            if (y<0.5):
                x+=1
            else:
                x-=1
            if x==0:
                count+=1    
        print(count, end=",")    
        



if __name__ == '__main__':
    helper()
