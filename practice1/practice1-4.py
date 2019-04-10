# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# practice1-4

# rooster -> 5, hen -> 3, 3chicks -> 1
# ￥100 -> 100

sum_ = 100 # the sum of hens, roosters and chicks
cost = 100
price_rooster = 5 # each rooster costs 5
price_hen = 3 # eaach hen costs 3
one4chick = 3 # 3 chicks costs 1


for rooster in range(sum_ // price_rooster + 1): # number of rooster no more than 25
    for hen in range(sum_ // price_hen + 1): # number of hen no more than 33
        chick = sum_ - rooster - hen
        if chick % one4chick == 0 and (price_rooster * rooster + price_hen * hen + chick / one4chick) == cost: # 3 chicks -> 1 and cost = 100
            print("rooster:{}, hen:{}, chick:{}".format(rooster, hen, chick))
        else:
            pass
