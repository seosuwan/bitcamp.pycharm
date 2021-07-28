import matplotlib.pyplot as plt
import numpy as np
'''
np.random.randint(low=10, high=100, size=200)
low~higj 추출되는 숫자의 범의
size 추출되는 데이터의 숫자
'''


def show_numpy():
    t = np.arange(0., 5., 0.2)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()


def numpy_choice():
    dice = np.random.choice(6, 100000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
    plt.hist(dice, bins=6)
    plt.show()


def numpy_not_need_for_loop():
    x = np.random.randint(low=10, high=100, size=200) #(low, high=None, size=None, dtype=None)
    y = np.random.randint(10, 100, 200)
    size = np.random.randint(100) * 100

    plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)# scatter 점점 흩뿌려지는거
    plt.colorbar()
    plt.show()


def indexing_slicing():
    a = np.array([1, 2, 3, 4])
    print(f'list -> array {a}]') #[1 2 3 4] 리스트에,를 떼버렸다.
    print(f'indexing a[1] : {a[1]},indexing a[-1] :{a[-1]}')
    print(f'slicing a[1] :{a[1:]}')


def array_have_one_type():
    a = np.array([1, 2, '3', 4])
    print(f'int -> str{a}')


def np_zeros():
    print(np.zeros(10)) #0으로 이루어진 크기가 10인 배열생성


def np_ones():
    print(np.ones(10))


def np_eye():
    print(np.eye(3))


def np_arange():
    print(f'[0 1 2] : {np.arange(3)}')
    print(f'[3 4 5 6] : {np.arange(start=3, stop=7)}')
    print(f'[3 5] : {np.arange(start=3, stop=7, step=2)}')
    print(f'[1.  1.2 1.4 1.6 1.8] : {np.arange(start=1, stop=2, step=0.2)}')



def np_linspace():
    print(f'[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ] :{np.linspace(1, 2, 11)}')
    a = np.linspace(1, 2, 11)
    print(f'{np.sqrt(a)}')
    '''
    [1.         1.04880885 1.09544512 1.14017543 1.18321596 1.22474487
     1.26491106 1.30384048 1.34164079 1.37840488 1.41421356]

    '''


def np_mask():
    a = np.arange(-5, 5)
    print(f'[-5 -4 -3 -2 -1] : {a[a < 0]}')
    mask1 = abs(a) > 3
    mask2 = abs(a) % 2 == 0
    print(a[mask1])
    print(f'{[mask1+mask2]}') #java에서 || 연산
    print(f'{[mask1*mask2]}') #java에서 && 연산



if __name__ == '__main__':
    #show_numpy()
    #numpy_choice()
    #numpy_not_need_for_loop()
    #indexing_slicing()
    #np_ones()
    #np_eye()
    #np_arange()
    #np_linspace()
    np_mask()