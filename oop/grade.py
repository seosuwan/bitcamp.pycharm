'''
국어kor, 영어eng, 수학math 를 입력받아서
평균점수를 통해 A ~ F 학점을 출력하시오
'''
class Credit(object):

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math


    def sum(self):
        return (self.kor + self.math + self.eng)

    def average(self):
        return self.sum() / 3


    @staticmethod
    def main():
        while 1:
            menu = input('0 - EXIT 1- Score \n')
            kor = int(input('국어\n'))
            eng = int(input('영어\n'))
            math = int(input('수학\n'))
            cre = Credit(kor, eng, math)

            if menu == '0':
                return
            elif cre.average() >= 90:
                print('A')
                break
            elif cre.average() >= 80:
                print('B')
                break
            elif cre.average() >= 70:
                print('C')
                break
            elif cre.average() >= 60:
                print('D')
                break
            elif cre.average() >= 50:
                print('E')
                break
            else:
                print('F')
                break

Credit.main()