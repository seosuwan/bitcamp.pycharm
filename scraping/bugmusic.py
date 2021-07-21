from bs4 import BeautifulSoup
from urllib.request import urlopen
'''
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
'''


class Bugmusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):

        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artist = 0
        ls_artists = soup.findAll('p', {'class':'artist'})
        ls_title = soup.findAll('p', {'class':'title'})
        for i, j in enumerate(ls_artists):
            n_artist += 1
            print('Rank :' + str(n_artist), end='\t')
            print('Artist' + j.find('a').text)
            print('Title' + ls_title[i].find('a').text)

        '''
        for i in range(len(n_title)):
            title = n_title[i].text.strip().split('\n')[0]
            artist = n_artists[i].text.strip().split('\n')[0]
            print(':Rank: {} {} {}'.format(i+1, title, artist))
        '''

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'}
    Bugmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                        f'chartdate={20210720}&charthour={16}').scrap()


if __name__ == '__main__':
    main()