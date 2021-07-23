from bs4 import BeautifulSoup
import pandas as pd
import requests

from common.menu import print_menu


class MusicRanking(object):
    domain = ''
    query_string = ''
    url = ''
    html = ''
    tag_name = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    artists = []
    titles = []
    dict = {}
    fname = ''
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text


    def get_raking(self):
        soup = BeautifulSoup(self.html, 'lxml')
        _= 0
        artists = soup.findAll(self.tag_name, {'class': self.class_name[0]})
        titles = soup.findAll(self.tag_name, {'class': self.class_name[1]})
        for i, j in zip(artists, titles):
            _ += 1
            print(f":RANK:{_} Artist: {i.find('a').text} Title: {j.find('a').text}")
            self.artists.append(i.find('a').text)
            self.titles.append(j.find('a').text)

        print(self.titles)
        print(self.artists)




    def insert_dict(self):
        '''for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]'''
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        print(self.dict)
    def dict_to_dataframe(self):
        dict = self.dict
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)
    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')




def main():
    mr = MusicRanking()
    while 1:
        menu = print_menu(['EXIT', 'Music Url', 'Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        if menu == 0:
            break
        elif menu == 1:
            menu2 = print_menu(['Bugs', 'Melon'])
            if menu2 == 0:
                mr.fname = 'Bugsmusic'
                mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
                mr.query_string = 'chartdate=20210720&charthour=16'
            elif menu2 == 1:
                mr.fname = 'Melonmusic'
                mr.domain = 'https://www.melon.com/chart/index.htm?'
                mr.query_string = 'dayTime=2021072100'
            mr.set_html()
        elif menu == 2:
            if menu2 == 0:
                mr.class_name.append('title')
                mr.class_name.append('artist')
                mr.tag_name = 'p'
            elif menu2 == 1:
                mr.class_name.append('ellipsis rank02')
                mr.class_name.append('ellipsis rank01')
                mr.tag_name = 'div'
            mr.get_raking()

        elif menu == 3:
            mr.insert_dict()
        elif menu == 4:
            mr.dict_to_dataframe()
        elif menu == 5:
            mr.df_to_csv()


if __name__ == '__main__':
    main()
