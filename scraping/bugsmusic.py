from bs4 import BeautifulSoup
from urllib.request import urlopen
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


        
        
        



def main():
    Bugsmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                        f'chartdate={20210720}&charthour={16}').scrap()


if __name__ == '__main__':
    main()