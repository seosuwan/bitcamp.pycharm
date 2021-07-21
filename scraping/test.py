from bs4 import BeautifulSoup
import pandas as pd
import requests

class MusicRanking(object):
    domain = ''
    query_string = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        print(f'Crawling HTML is {self.html}')
    def get_raking(self):
        soup = BeautifulSoup(self.html, 'lxml')

def print_menu(ls):
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))

def main():
    # 20210720
    # 16
    mr = MusicRanking()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV' ])
        # 0- exit, 1- Bugs (URL), 2- Melon (URL) 3- output, 4-print dict,
        # 5-dict to dataframe, 6-df to csv
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=09'
            mr.set_html()

        elif menu == 2:
            mr.class_name.append('ellipsis rank02')
            mr.class_name.append('ellipsis rank01')
            mr.get_raking()
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass

if __name__ == '__main__':
    main()