# -*-coding:utf-8-*-
# created by HolyKwok 201610414206
# practice1-1

# detect the quality of the air

def air_detection(air_data):
    # a function for air detection
    
    if air_daata >= 250 : # severe pollution
        print(u'严重污染')
    elif air_data >= 150: # heavy pollution
        print(u'重度污染')
    elif air_data >= 115: # middle poluution
        print(u"中度污染")
    elif air_data >= 75: # light pollution
        print(u"轻度污染")
    elif air_data >= 35: # good
        print(u'良')
    elif air_daata >=0: # awesome
        print(u'优')
    else:
        print(u'输入错误')

if __name__ == '__main__':
    try:
        air_daata = eval(input(u'今日空气质量:')) # 输入空气数据
        air_detection(air_daata)
    except Exception:
        print(u"输入格式不正确！")