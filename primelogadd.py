from math import sqrt
from math import log

def primeadd(num):
  number = int(num)
  count = 0
  candi = 1
  addon = 0
  while candi < number:
    candi += 1
    for k in range(2, 1+int(sqrt(candi+1))):
        if candi%k == 0:       
            break
    else:    
        addon+=log(candi)
        count += 1                
  return addon

n=input("please enter the number:")
add = primeadd(n)

print(add,n,add/int(n))
