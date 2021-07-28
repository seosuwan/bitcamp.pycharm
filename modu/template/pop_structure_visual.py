import csv
import numpy as np
import matplotlib.pyplot as plt

class Population():

    data: [] = list()
    name: [] = list()
    home: [] = list()

    def read_data(self):
        data = csv.reader(open('data/population.csv', 'rt', encoding='UTF-8'))#csv는 일회성 한번쓰면 GC가 제거한다
        next(data)
        #print([i for i in data])
        self.data = data
    '''
    def pop_per_dong(self, dong:str) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]] #for문이 두번 도니까 append에 j를 넣는다
        print('*'*100)
        return arr

    def show_plot(self, arr:[]):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()
    '''

    def numpy_population(self, name: str):
        self.name = name
        for i in self.data:
            if name in i[0]:
                self.home = np.array(i[3:], dtype=int) / int(i[2])

    def show_numpy_population(self):
        plt.rc('font', family='Malgun Gothic')
        plt.title(self.name+ '지역의 인구구조')
        plt.plot(self.home)
        plt.show()

if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    #pop.show_plot(pop.pop_per_dong('역삼2동'))
    pop.numpy_population(input('인구 구조가 알고 싶은 지역의 이름(읍,면,동)을 입력해주세요\n'))
    pop.show_numpy_population()


