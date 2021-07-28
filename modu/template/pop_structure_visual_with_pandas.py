import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


# data = csv.reader(open('data/population.csv', 'rt', encoding='UTF-8'))#csv는 일회성 한번쓰면 GC가 제거한다

class Population():

    away: object = None
    data: [] = list()
    home: [] = list()
    result_name: str = ''
    def read_data(self):
        df = pd.read_csv('./data/population.csv', encoding='UTF-8', thousands=',', index_col=0)
        df.to_csv('./data/population_1.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('./data/population_1.csv', 'rt', encoding='UTF8'))
        #print([i for i in data])

        next(data)
        self.data = list(data)

    def pop_per_dong(self, dong:str) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]] #for문이 두번 도니까 append에 j를 넣는다
        print('*'*100)
        return arr

    def show_plot(self, arr:[]):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()


    def numpy_population(self, name: str) -> []:
        home = []
        [home.append(int(j)) for i in self.data if name in i[0] for j in i[3:]]
        self.home = home

    def show_numpy_population(self, arr:object, name: str):
        plt.title(f'{name} 지역의 인구구조')
        plt.plot(arr)
        plt.show()

    def array_to_list(self, arr) -> []:
        return arr.tolist()

    def list_to_array(self, ls: []) -> object:
        return np.array(ls)

    def find_similar_area(self, name: str):
        mn =1
        result = 0
        home = []
        for i in self.data:
            if name in i[0]:
                home = np.array(i[3:], dtype=int)/int(i[2])
        self.home = home

        for i in self.data:
            away = np.array(i[3:], dtype=int)/int(i[2])
            s = np.sum((self.home - away) ** 2)
            if s < mn and name not in i[0]:
                mn = s
                self.result_name = i[0]
                result = away
        self.away = result

    def show_plot_similar_two_cities(self, name: str, home: [], away: []):
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.title('필동 지역과 가장 비슷한 인구 구조를 가진 지역')
        plt.plot(away, label=name)
        plt.plot(home, label=self.result_name)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    pop.numpy_population('필동')
    pop.home = pop.list_to_array(pop.home)
    pop.find_similar_area('필동')
    pop.show_plot_similar_two_cities('필동', pop.home, pop.away)