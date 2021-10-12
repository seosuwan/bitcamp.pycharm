from dataclasses import dataclass
# Create your models here.
# from django.db import models


@dataclass
class Palindrome(object):
    input_string: str

    @property
    def input_string(self) -> str: return self._input_string

    @input_string.setter
    def input_string(self, input_string): self._input_string = input_string

    def str_to_list(self) -> []:
        return [i for i in self.input_string if i.isalnum()]

    def isPalindrome(self) -> bool:
        ls = self.str_to_list()
        print(f'ls len : {len(ls)}')
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}
        # return [i for i in ls if ls.pop(0) != ls.pop()]

    def reverse_string(self) -> []:
        strs = self.str_to_list()
        return strs[::-1]
        pass

class Palindrome2(object):

    def str_to_list(self, list) -> [] :
        return [i for i in list if i.isalnum()]


    def isPalindrome(self, ls: []) -> bool:
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}
    #
    # def str_to_list(payload: str) -> []:
    #     return []

    def reverse_list(self, ls: []) -> []:
        return ls[::-1]

    def list_to_str(self, ls: []) -> str:
        return ''