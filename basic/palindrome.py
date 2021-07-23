def str_to_list(payload: str) -> []:

    strs = []
    for char in payload:
        if char.isalnum():
            strs.append(char.lower())
    return strs


def is_palindrome(ls: []) -> bool:
    while len(ls) > 1:
        if ls.pop(0) != ls.pop():
            return False
    return True


if __name__ == '__main__':
    ls = str_to_list('A man, a plan, a canal: Panama')
    print(ls)
    isp = is_palindrome(ls)
    print(isp)

