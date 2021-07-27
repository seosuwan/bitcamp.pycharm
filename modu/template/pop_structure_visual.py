import csv

import matplotlib.pyplot as plt

class Population():

    data: [] = list()

    def read_data(self):
        data = csv.reader(open('data/population.csv', 'rt', encoding='UTF-8'))#csv는 일회성 한번쓰면 GC가 제거한다
        next(data)
        #print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong:str) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]] #for문이 두번 도니까 append에 j를 넣는다
        print('*'*100)
        return arr

    def show_plot(self, arr:[]):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()

if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    pop.show_plot(pop.pop_per_dong('역삼2동'))

