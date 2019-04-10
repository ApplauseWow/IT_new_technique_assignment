# -*-coding:utf-8-*-
# created by holykwok 201610414206
# practice1-5

# each step -> 1 or 2 or 3

# method1-普通递归
def jump(step):
    # 剩step个台阶
    if step <= 0: # 异常台阶数
        return 0
    elif step == 1: # 台阶数为1的台阶有1种跳法
        return 1
    elif step == 2: # 台阶数为2的台阶有2种跳法
        return 2 # jump(1)+1
    elif step == 3: # 台阶数为3的台阶有4种跳法
        return 4 # jump(1) + jump(2) + 1
    else: 
        return jump(step - 3) + jump(step - 2) + jump(step - 1) # 到第step个可以从step-3跳3步跳法有已知的jump(step-3)种，以此类推也可以从step-2和step-1跳

# method2-尾递归(秒解50阶)
def jump2(step, num = 0, strategy = 0, pre_strategy = []): 
    '''
    跳到step阶有strategy种方式，到距离第step台阶1, 2, 3阶的跳法分别是[a, b, c]
    step: 总台阶数
    num: 计步器
    strategy: 到当前台阶跳法
    pre_strategy: 前三个台阶的跳法
    '''
    
    if step <= 0: # 非法台阶数
        return 0
    else:
        if num == step: # 到达最后的台阶
            return strategy
        else: # 没有到达最后的台阶 
            strategy = sum(pre_strategy) # 调到第num个台阶的跳法等于距其1,2,3个台阶的跳法， sum([])的和等于0
            if num < 3: # 前3个台阶的跳法
                strategy += 1 # 在之前的跳法上加上本身的一种跳法
            pre_strategy.append(strategy) # 将此时台阶的跳法加入列表
            num += 1
            return jump2(step, num, strategy, pre_strategy[-3:]) # 只取距下一个台阶1,2,3的台阶跳法即只取后三个，[1,2][-3:]切片也为[1,2]
            
print(jump(20))
print(jump2(20), jump2(50))