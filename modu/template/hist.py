import matplotlib.pyplot as plt
import random

from modu.template import TemperatureChangedMyBirthday

'''
consumer는 리턴을 따로준다
'''


def hist_show():
    plt.plot([1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 10])
    plt.show()


def dice_show(count):
    dice = []
    [dice.append(random.randint(1, 6)) for i in range(count)]
    return dice


def show_hist(dice):
    plt.hist(dice, bins=6)
    plt.show()


def highest_temperature(month: str) -> []:
    arr = []
    birht = TemperatureChangedMyBirthday()
    # [print(i) for i in birht.data]
    birht.read_data()
    next(birht.data)
    [arr.append(float(i[-1]))for i in birht.data if i[-1] != '' if i[0].split('-')[1] == month]
    return arr #append()는 cosumer이기 때문에 리턴값이 NoneType 다른곳에서 쓰려면 return을 해야한다


def show_hist_about(aug: [], month: str):
    plt.hist(aug, bins=100, color='r', label=f'{month}Month')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    #dice = dice_show(1000000)
    #print(dice)
    #show_hist(dice)
    show_hist_about(highest_temperature('09'), month='01')

