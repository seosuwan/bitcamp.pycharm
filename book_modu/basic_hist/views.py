from book_modu.basic_hist.models import BasicHist

if __name__ == '__main__':
    # hist_show(dice(int(input('How much?'))))
    # ls = []
    # while 1:
    #     menu = int(input('1. add else. show'))
    #     [ls.append(highest_temperature(input('Month?'))) if menu == 1 else hist_show_many(ls)]
    a = BasicHist()
    a.show_hist_about(a.highest_temperature('02'), '02')