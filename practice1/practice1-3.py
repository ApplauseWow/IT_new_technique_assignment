# -*-coding:utf-8-*-
# created by holykwok 201610414206
# practice1-3

# the sum of prime number within 1000 

from math import sqrt

def is_a_prime(num):
    '''
    to check it if it's a prime
    '''
    
    # i_ = math.sqrt(i)
    for i in range(2, int(sqrt(num) + 1)): # except 1 and itself, 1*8 2*4 4*2 8*1 ,2 to sqrt(self)
        # for(i=2, 1 <= sqrt(i), i++) each loop excutes the sqrt(), but it excutes once by range() method in python
        if num % i == 0: # not a prime
            return False
        else:
            pass
    return True

sum_ = 2 # every prime number is odd except 2, and 1 is not a prime
border = 1000
for i in range(3, border + 1, 2): # 3 5 7...2n+1
    if is_a_prime(i): # a prime
        # print(i)
        sum_ += i # 1 + 2 + 3 + 5 + ... + 2n+1
    else: # not a prime
        pass
print(sum_)