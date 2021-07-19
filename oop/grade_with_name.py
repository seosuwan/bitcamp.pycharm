'''
국어kor, 영어eng, 수학math 를 입력받아서
평균점수를 통해 A ~ F 학점을 출력하시오
'''


class Credit(object):

    def __init__(self,  name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)


    def avg(self):
        return sum(self.scores) / len(self.scores)


    @staticmethod                        # 이름 평균점수 학점
    def main():
        cre = Credit(input('Input Student Name:'))
        '''
        kor = int(input('국어\n'))
        eng = int(input('영어\n'))
        math = int(input('수학\n'))
        '''

        for i in ['국어', '영어', '수학']:
            cre.addScores(int(input(f'{i}:')))

        avg = cre.avg()
        if avg >= 90:
            result = 'A'

        elif avg >= 80:
            result = 'B'

        elif avg >= 70:
            result = 'C'

        elif avg >= 60:
            result = 'D'

        elif avg >= 50:
            result = 'E'

        else:
            result = 'F'
        print(f'{result}')


Credit.main()