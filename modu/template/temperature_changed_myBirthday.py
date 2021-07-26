import csv
import matplotlib.pyplot as plt
'''
next()는 function 구조로 사용되면 header만 리턴한다
comsumer 구조로 사용되면 데이터에서 header를 제거한다.
row[] = 날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃) 최고기온은 [-1]이다.
data : [] = list() 는  list타입의 data를 list()로 초기화 시킴
단, 한 메소드 내에서만 사용하면 로컬에서 초기화 예제
data : [] = None
def save_highest_temperature(self):
    data = list()
그러나 여러 메소드에서 사용하면 필드에서 초기화 됌
data : [] = list
'''
class TemperatureChangedMyBirthday(object):
    data: [] = list()
    highest_temperature: [] = list()

    def processing(self):  #훅을 걸어서 메소드 순서정하기
        self.read_data
        self.save_data_to_list
        self.visualizing_data
        self.extracting_date_data

    def read_data(self) -> object:
        data = csv.reader(open('./data/unit_5_seoul.csv', 'rt', encoding = 'UTF-8'))
        next(data)
       # print([i for i in data])
        self.data = data
        return data

    def show_highest_temperature(self):
        return [i[-1] for i in self.data]

    def save_highest_temperature(self):
        [self.highest_temperature.append(float(i[-1])) for i in self.data if i[-1] != '']
        print({len(self.highest_temperature)})

    def visualizing_data_highest_temperature(self):
        plt.plot(self.highest_temperature(), 'r')
        plt.figure(figsize=(10, 2))
        plt.show()

    def highest_temperatures_my_birthday(self):
        high = []
        low = []
        for i in self.data:
            if i[-1] != '' and i[-2] != '':
                if 1983 <= int(i[0].split('-')[0]):
                    if (i[0].split('-')[1] == '02') and i[0].split('-')[2] == '14':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))
        plt.plot(high, 'hotpink')
        plt.plot(low, 'skyblue')
        plt.show() #comsumer print할거 없음.

def date(full_date):
    pass



if __name__ == '__main__':
    this = TemperatureChangedMyBirthday()
    this.read_data()
    #this.save_highest_temperature()
    this.highest_temperatures_my_birthday()



