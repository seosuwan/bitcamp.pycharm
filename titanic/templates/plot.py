from titanic.model.dataset import Dataset
from titanic.model.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())
'''
titanic's features
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
'''


class Plot(object):
    dataset = Dataset()
    service = Service()

    def __init__(self):
        self.df = self.service.new_model('train.csv')# object is DataFrame

    def show_plot_survived_dead(self): #매트리스 차원 올라감
        this = self.df # df = 행렬
        f, ax = plt.subplots(1, 2, figsize= (18, 8))
        series = this['Survived'].value_counts() # series가 리스트
        print(type(series)) #행, 열 series가 모여서 df /df 에서 요소(series)를 뽑아낸다
        print(series)
        series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def show_plot_pclass(self):
        this = self.df
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['좌석등급'] = this['Pclass'].replace(1, '일등석').replace(2, '이등석').replace(3, '삼등석')
        sns.countplot(data=this, x='좌석등급', hue='생존결과')
        plt.show()

    def show_plot_embarked(self):
        #c = 쉘버그 ,s = 사우스햄튼 q = 퀸즈타운
        this = self.df
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['승선항구'] = this['Embarked'].replace('C', '쉘버그').replace('S', '사우스햄튼').replace('Q', '퀸즈타운')
        sns.countplot(data=this, x='승선항구', y='좌석등급' , hue='생존결과')
        plt.show()

    def show_plot_sex(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize=(18, 8)) #ax가 축
        male_series = this['Survived'][this['Sex'] == 'male'].value_counts() #전체에서 두개의 시리즈를 뽑아온다
        female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
        male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율 0.사망자 vs 1.생존자')
        ax[1].set_title('여성의 생존비율 0.사망자 vs 1.생존자')
        plt.show()



