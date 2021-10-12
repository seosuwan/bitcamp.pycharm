from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

'''
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
'''


class Bugsmusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        '''
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artists = soup.findAll('p', {'class': 'artist'})
        n_title = soup.findAll('p', {'class': 'title'})
        for i in range(len(n_title)):
            title = n_title[i].text.strip().split('\n')[0]
            artist = n_artists[i].text.strip().split('\n')[0]
            print(':Rank: {} {} {}'.format(i+1, title, artist))

        '''
        _= 0
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        artists = soup.findAll('p', {'class': 'artist'})
        titles = soup.findAll('p', {'class': 'title'})
        print(f'List size is{len(artists)}')
        for i, j in zip(titles, artists):
            _+= +1
            print(f":RANK:{_} Artist: {j.find('a').text} Title: {i.find('a').text}")

class Melonmusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})), 'lxml')
        n_artists = soup.findAll('div', {'class': 'ellipsis rank02'})
        n_title = soup.findAll('div', {'class': 'ellipsis rank01'})
        for i in range(len(n_title)):
            ellipsis_rank02 = n_title[i].find('a').text.strip().split('\n')
            ellipsis_rank01 = n_artists[i].find('a').text.strip().split('\n')
            print('RANK: {} {} {}'.format(i+1, ellipsis_rank01, ellipsis_rank02))



def main():
    Bugsmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                        f'chartdate={20210720}&charthour={16}').scrap()
if __name__ == '__main__':
    Melonmusic('https://www.melon.com/chart/index.htm?dayTime=2021072016').scrap()


from bs4 import BeautifulSoup
import pandas as pd
import requests


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
