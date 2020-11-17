from gpio import GPIO
import time

def decToBinList(decNumber):
    s = [0,0,0,0,0,0,0,0]
 value=bin(decNumber)
 p = 7
 for i in reversed(value):
     if i=='b':
        break
     elif i=="1":
          s[p]=1
     else:
         s[p]=0
     p = p - 1
 return (s)
