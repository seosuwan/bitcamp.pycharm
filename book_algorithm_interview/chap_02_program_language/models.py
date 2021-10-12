from dataclasses import dataclass


class OneToTenSum(object):

    def one_to_ten_sum_1(self):
        # example 1
        sum = 0
        for i in range(1, 11):
            sum += i
        return sum

    def one_to_ten_sum_2(self):
        vul = sum(i for i in range(1, 11))
        return vul

        # 예시 3

    def one_to_ten_sum_3(self):
        vul = sum(range(1, 11))
        return vul

@dataclass
class MySum(object):

    start_number: int
    end_number: int

    @property
    def start_number(self)-> int: return self._start_number

    @property
    def end_number(self) -> int: return self._end_number

    @start_number.setter
    def start_number(self, start_number): self._start_number = start_number

    @end_number.setter
    def end_number(self, end_number): self._end_number = end_number

    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(self.start_number, self.end_number):
            sum += i
        return sum

    def one_to_ten_sum_2(self):
        return sum(i for i in range(self.start_number, self.end_number))

    def one_to_ten_sum_3(self):
        return sum(range(self.start_number, self.end_number))