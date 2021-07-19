'''
이름 나이 주소를 입력받아서 자기 소개하는 프로그램 작성
출력은 안녕하세요, 제이름은 Tom이고, 나이는 28세이고 서울에서 거주합니다. 로 됩니다.
이때, 여러 사람이면 전부 입력받아서 전체가 일괄 출력되는 시스템이어야 합니다.
'''

class Person(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


    def to_string(self):
        print(f'안녕하세요, 제 이름은{self.name}이고,나이는{self.age},{self.address}에서 거주합니다.')


    @staticmethod
    def main():
        count = int(int(input('How many ?')))
        people = []
        for i in range(count):
            person = Person(input('name'), input('age'), input('address'))
            people.append(person)
        for person in people:
            person.to_string()


Person.main()