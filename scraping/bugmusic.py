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
        n_artists = 0
        n_title = 0
        for i in soup.findAll(name= 'p', attrs={'class':'artist'}):
            n_artists += 1
            print(str(n_artists) +  "Rank")
            print("Artists : " + i.find('a').text)



def main():
    Bugmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                        f'chartdate={input("Input Date")}&charthour={input("Input Hour")}').scrap()


if __name__ == '__main__':
    main()