def str_to_list(payload: str) -> []:
    return [i for i in payload if i.isalnum()]


def reverse_string(s: []) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    return s

def list_to_str(s: []) -> str:
    pass



if __name__ == '__main__':
    re = str_to_list('HELLO WORLD')
    print(re)
    print(re)
    print(re)
    print(re)
    re1 = reverse_string(re)
    print(re1)

