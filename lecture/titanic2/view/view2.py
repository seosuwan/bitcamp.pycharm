from lecture.titanic2.model.dataset import Dataset
from lecture.titanic2.model.service import Service


class View2(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        this = self.preprocessing(train, test)
        print(f'The Type of This is {type(this.train)}')
        print(f'The Type of This is \n {this.train.head(2)}')
        print(f'The Type of This is \n {this.test.head(2)}')

    def preprocessing(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        return this

if __name__ == '__main__':
    view = View2()
    view.modeling('train.csv', 'test.csv')

