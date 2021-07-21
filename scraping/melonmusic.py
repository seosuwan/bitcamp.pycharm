from bs4 import BeautifulSoup
from urllib.request import urlopen

class Melonmusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lmxl')
        n_artists = soup.findAll('div', {'class':'ellipsis rank02'})
        n_title = soup.findAll('div', {'class':'ellipsis rank01'})
        for i in range(len(n_title)):
            title = n_title[i].text.strip().split('\n')
            artist = n_artists[i].text.strip().split('\n')
            print('RANK: {} {} {}'.format(i+1, title, artist))


def main():
    Melonmusic (f'https://www.melon.com/chart/index.htm?dayTime=2021072100').scrap()


if __name__ == '__main__':
    main()