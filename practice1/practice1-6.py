# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# practice1-6

# a toy car -> ￥x, use ￥y for z cars, so how to pay less change

val = [50, 20, 10, 5, 1] # 面额
num = [0, 0, 0, 0, 0] # 找零张数
price = 13 # 单价

def pay_change(left):
    # left: the money left
    
    if left == 0: # 没有可找零钱
        return
    for v in val:
        if left >= v: # 可找此面额
            num[val.index(v)] += 1
            return pay_change(left - v)
        else: 
            pass
        
try:
    num_car = int(eval(input(u'请输入购买个数:'))) # 输入购买个数 
    money = int(eval(input(u'请输入购买金额:'))) # 输入购买个数
    if num_car <= 0 or money <=0: # 非法数量，支付数
        print(u'输入错误')
    else:
        left = money - price * num_car # 找零
        if left < 0: # 支付不够
            print(u'请给足够的金额')
        elif left == 0: # 不找零
            print(u'没有零钱')
        else: # 找零
            pay_change(left)
            print(u'应找零:', left)
            for x, y in zip(val, num):
                if y > 0: # 需找零面额
                    print(u"面值{}:{}张".format(x, y))
except Exception:
    print(u"输入格式不正确！")
