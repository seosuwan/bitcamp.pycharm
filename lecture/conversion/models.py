import pandas as pd
from icecream import ic

class Conversion(object):
    def __init__(self):
        print('자료구조 타입변환 예제')
        print('Q1. 1부터 9까지 요소를 갖는 튜플 생성')
        tpl = self.create_tuple()
        ic(type(tpl))
        ic(tpl)
        print('Q2. 튜플을 리스트로 전환')
        lst = self.tuple_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q3. 리스트의 int 값을 float 로 전환')
        lst = self.int_to_float(lst)
        ic(type(lst))
        ic(lst)
        print('Q4. float 리스트를 int 리스트 로 전환')
        lst = self.float_to_int(lst)
        ic(type(lst))
        ic(lst)
        print('Q5. int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함')
        dic = self.list_to_dictionary(lst)
        ic(type(dic))
        ic(dic)
        print('Q6. "hello"를 가진 튜플생성')
        tpl = self.hello_to_tuple('hello')
        ic(type(tpl))
        ic(tpl)
        print('Q7. 6번 튜플을 리스트로 전환')
        lst = self.hello_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q8. 5번 딕셔너리를 dataframe 으로 전환')
        df = self.dictionary_to_dataframe(dic)
        ic(type(df))
        ic(df)
        print('Q9. 1번 튜플의 제곱을 요소로 갖는 리스트 출력')
        tpl = self.tuple_square(self.create_tuple())
        ic(type(tpl))
        ic(tpl)
        print('Q10. 구구단 한 줄 출력 2*1=2, 2*2=4, ..., 9*9=81')
        tpl = self.multiplication(self.create_tuple())
        ic(type(tpl))
        ic(tpl)
        print('Q11. 1번 튜플에서 3의 배수만 문자열로 갖는 리스트 출력')
        tpl = self.three_multi_change_str(self.create_tuple())
        ic(type(tpl))
        ic(tpl)

    #Q1. 1부터 9까지 요소를 갖는 튜플 생성
    def create_tuple(self) -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9)

    #Q2. 튜플을 리스트로 전환
    def tuple_to_list(self ,tpl) -> []:
        #list(tpl)
        return [i for i in tpl]

    #Q3. 리스트의 int 값을 float 로 전환
    def int_to_float(self, tpl) -> []:
        return [float(i) for i in tpl]

    #Q4. float 리스트를 int 리스트 로 전환
    def float_to_int(self,tpl) -> []:
        return [int(i) for i in tpl]

    #Q5. int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함
    def list_to_dictionary(self, tpl) -> {}:
        return {str(i): f'value-{i}' for i in tpl}

    #Q6. "hello"를 가진 튜플생성
    def hello_to_tuple(self ,param:str) -> ():
        return tuple(param)

    #Q7. 6번 튜플을 리스트로 전환
    def hello_to_list(self , param) -> []:
        return list(param)

    #Q8. 5번 딕셔너리를 dataframe 으로 전환
    def dictionary_to_dataframe(self,dic) -> object:
        return pd.DataFrame.from_dict(dic, orient='index')


    #Q9. 1번 튜플의 제곱을 요소로 갖는 리스트 출력
    def tuple_square(self, tpl) -> []:
        return list(map(lambda x: pow(x,2),tpl))

        #Q10. 구구단 한 줄 출력 2*1=2, 2*2=4, ..., 9*9=81
    def multiplication(self,tpl) -> []:
        return list(map(lambda x: [f'{x}x{i}={x * i}' for i in range(1,10)],tpl)) #열 , 행 가장밖에있는게 행 !행!

    #Q11. 1번 튜플에서 3의 배수만 문자열로 갖는 리스트 출력
    def three_multi_change_str(self,tpl) -> []:
        return list(map(lambda x: str(x) if x % 3 == 0 else x,tpl))

if __name__ == '__main__':
    Conversion()






