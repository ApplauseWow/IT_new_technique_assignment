import random
import matplotlib
import matplotlib.pyplot as plt
import numpy

# def list2mat(data_list, w):
#     '''
#     切片、转置
#     '''
#     mat = []
#     res = []
#     for i in range(0, len(data_list) - w + 1, w):
#         mat.append(data_list[i:i + w])
#     for i in range(len(mat[0])):
#         one_list = []
#         for j in range(len(mat)):
#             one_list.append(mat[j][i])
#         res.append(one_list)
#     return res


def draw_pic_test(data_list, y_data, output):
    '''
    作图
    '''

    plt.rcParams['figure.figsize'] = (8.0, 5.0) # 图片长宽比例
    plt.rcParams['savefig.dpi'] = 500  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率

    fig, ax = plt.subplots()
    # mat = list2mat(data_list, w=10)
    for one_list in data_list:
        one_list = [int(one) for one in one_list]
        y_data = [int(one) for one in y_data]
        zipped = list(zip(one_list, y_data))
        result = sorted(zipped)
        div = list(zip(*result))
        x = div[0]
        y = div[1]
        # ax.plot(x, y)
        plt.plot(x, y, "-", label="test_zhexian")
    # plt.xticks(numpy.arange(0, 40, 0.1), ())
    # plt.tick_params(axis='x', labelsize='medium', width=25)
    # plt.show()
    plt.savefig(output)
    plt.close()


if __name__ == '__main__':
    data_list = []
    with open('data', 'r') as f:
        lines = f.readlines()
        for l in lines:
            l = l.split()
            data_list.append(l)

    y_data = data_list[-1][:]
    data_list.pop(-1)
    draw_pic_test(data_list, y_data, "10.png")

    # data_list = []
    # with open('data2', 'r') as f:
    #     lines = f.readlines()
    #     for l in lines:
    #         l = l.split()
    #         data_list.append(l)
    #
    # y_data = data_list[-1][:]
    # data_list.pop(-1)
    # draw_pic_test(data_list, y_data, "2.png")

