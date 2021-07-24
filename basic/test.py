def str_to_list(str):
    s = []
    for i in str:
        s.append(i)
    return s


def reverse(list):
    d = []
    a = len(list)
    for i in range(len(list)):
        d.append(list.pop())
        # d.append(list.pop())
    return d




if __name__ == '__main__':
    ss = str_to_list('HELLO')
    print(ss)
    ss1 = reverse(ss)
    print(ss1)
