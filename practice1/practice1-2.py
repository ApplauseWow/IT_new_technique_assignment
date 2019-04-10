# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# practice1-2

# 5 monkeys, each of them eats one peach and divide the rest into 5 parts and takes one of the parts...

monkey = 5 # number of monkey
ate = 1 # each time eats one peach
num = 1 # from 1 to the smallest

def find_out_smallest(receiver, time):
    '''
    找出最小的满足条件的数
    receiver: 所需验证的数
    time: 验证次数
    '''
    
    if time == 0: # 验证完毕
        return True
    else: # 继续验证
        if (receiver - ate) % monkey == 0: # 满足条件
            receiver = (receiver - 1) / monkey * (monkey - 1)
            return find_out_smallest(receiver, time - 1)
        else: # 不满足条件
            return False
        
while True: # find out the smallest
    if find_out_smallest(num, monkey): # 找到满足条件的数
        break
    else: # 继续找
        num += 1
print(num)