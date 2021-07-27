import matplotlib.pyplot as plt
import random

from modu.template import TemperatureChangedMyBirthday
from modu.template.hist import highest_temperature


def sorted_random_arr() -> []:
    arr = []
    [arr.append(random.randint(1, 1000))for i in range(13)]
    return arr


def show_boxplot(arr: []):

    plt.boxplot(arr)
    plt.show()

def show_boxpolt_month(month: str):
    arr = highest_temperature(month)
    plt.boxplot(highest_temperature(month))
    plt.show()


def show_boxplot_all_month():
    birth = TemperatureChangedMyBirthday()  # class 불러와서 쓰기
    birth.read_data()  # 데이터를 읽기위해
    arr = birth.data
    month = []
    [month.append([])for i in range(12)]
    [month[int(i[0].split('-')[1])-1].append(float(i[-1])) for i in arr if i[-1] !='']
    plt.boxplot(month)
    plt.show()


def show_boxplot_per_date(month: str):
    birth = TemperatureChangedMyBirthday()  # class 불러와서 쓰기
    birth.read_data()  # 데이터를 읽기위해
    arr = birth.data  # 데이터를 쓰기위해
    day = []  # 하루를 넣을 배열만들기
    [day.append([]) for i in range(31)]  # 배열 31개 만들기
    [day[int(i[0].split('-')[2]) - 1].append(float(i[-1]))
        for i in arr
            if i[-1] != ''
                if i[0].split('-')[1] == month]
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5), dpi=300)
    plt.boxplot(day, showfliers=False) #Omit Outlier
    plt.show()


if __name__ == '__main__':
    #show_boxplot(sorted_random_arr())
    #show_boxpolt_month('08')
    #show_boxplot_all_month()
    show_boxplot_per_date('08')