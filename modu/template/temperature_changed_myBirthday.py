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
    data: [] = list() #csv를 담을 data배열
    highest_temperature: [] = list() # 최고기온을 담을 배열

    def processing(self):  #훅을 걸어서 메소드 순서정하기
        self.read_data
        self.save_data_to_list
        self.visualizing_data
        self.extracting_date_data

    def read_data(self) -> object:
        data = csv.reader(open('data/seoul.csv', 'rt', encoding='UTF-8'))
        next(data)
       # print([i for i in data])
        self.data = data
        return data

    def show_highest_temperature(self):
        return [i[-1] for i in self.data] # i에 담겨있는 -1번째 인덱스를 모두 가져와

    def save_highest_temperature(self):
        [self.highest_temperature.append(float(i[-1])) for i in self.data if i[-1] != '']#1. 배열에 담는것 2.조건이있다는것
        print({len(self.highest_temperature)}) #최고기온을 담은 배열에 실수로된 -1인덱스 와 모든 데이터를 담은 data에서 마지막 인덱스와 비교해서 공백이 없으면 갖구왕

    def visualizing_data_highest_temperature(self):
        plt.plot(self.highest_temperature(), 'r')
        plt.figure(figsize=(10, 2))
        plt.show()

    def highest_temperatures_my_birthday(self):
        high = [] #  최고기온을 담을 배열
        low = [] #최저기온을 담을 배열
        for i in self.data:
            if i[-1] != '' and i[-2] != '': # 조건문 csv에 있는 인덱스 -1 뒤에서 첫번째 와 두번째가 공백이 없을경우
                if 1983 <= int(i[0].split('-')[0]): # 정수로된 csv에 0번째를 분할해서 분할한것에 인덱스 0번째를 1983보다 작거나 같을때 가지고 와 split()은 기본적으로 문자열공백 자름
                    if (i[0].split('-')[1] == '02') and i[0].split('-')[2] == '14':# csv에 0번째 인덱스 를 자른것에 1번째 인덱스와  02를 비교 그리고 2번째인덱스와 14를 비교
                        high.append(float(i[-1])) #실수로 된 -1번째 인덱스를 high에 담아라
                        low.append(float(i[-2])) #실수로 된 -2번째 인덱스를 low에 담아라
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일 기온 변화 그래프')
        plt.plot(high, 'hotpink', label='high')
        plt.plot(low, 'skyblue', label='low')
        plt.legend()
        plt.show() #comsumer print할거 없음.

def date(full_date):
    pass



if __name__ == '__main__':
    this = TemperatureChangedMyBirthday()
    this.read_data()
    print(this.show_highest_temperature())
    #this.save_highest_temperature()
    #this.highest_temperatures_my_birthday()



