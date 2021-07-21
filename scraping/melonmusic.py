from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

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
    Melonmusic(f'https://www.melon.com/chart/index.htm?dayTime={2021072100}').scrap()


if __name__ == '__main__':
    main()