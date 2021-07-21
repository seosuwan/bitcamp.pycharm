'''
주소, 이메일, 전화번호 이름
'''


class Contacts():
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'이름{self.name},전화번호{self.phone},이메일{self.email},주소{self.address}')


def set_contact():
    return Contacts(input('name'), input('phone'), input('email'), input('address'))


def get_contact(ls):
    for i in ls:
        i.to_string()


def del_contact(ls, name):
    for i, j in enumerate(ls):
        if name == j.name:
            del ls[i]


def print_menu():
    ls = ['EXIT', 'Add', 'Print', 'Delete']
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))
    '''
    for index, value in enumerate(ls):
        print(index, value)
        return '\t'.join(ls)
        '''


def main():
    ls = []
    while 1:
        menu = print_menu()
        if menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contact(ls)
        elif menu == 3:
            del_contact(ls, input('Del Name'))
        else:
            break


if __name__ == '__main__':
    main()