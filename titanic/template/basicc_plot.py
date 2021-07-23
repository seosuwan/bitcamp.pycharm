import matplotlib.pyplot as plt

from common.menu import print_menu

"""
list 값은 y 축이고, x축은 0부터 1까지 자동으로 증가한다.
범례 위치 직접 지정은 legend()함수안에 loc 값을 넣어주면 된다. plt.legend(loc = 5)
"""
def plot_show():
    plt.title('plotting')
    plt.plot([10, 20, 30, 40], label='asc')
    plt.legend()
    plt.show()


"""
첫번째 list 가 x 축이고, 두번째 list 가 y 축이다.
"""
def plot_two_list_show():
    plt.title('legend')
    plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='asc')
    plt.plot([40, 30, 20, 10], color='y', ls=':', label='dsec')
    plt.legend() #범례표시
    plt.show()


def plot_marker():
    plt.title('marker')
    plt.plot([10,20,30,40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = print_menu(['EXIT', 'Music Url', 'Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_marker()
