from common.menu import print_menu
from modu.template.basic_plot import plot_show, plot_two_list_show, plot_marker

if __name__ == '__main__':
    while 1:
        menu = print_menu(['EXIT', 'plot_show', 'plot_two_list_show', 'maker', 'scatter'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_marker()
        elif menu == 4:
            pass