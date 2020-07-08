import urllib3
from requests import get
from bs4 import BeautifulSoup
from re import sub

import parameters_search
import parameters_view

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class KoreanStandardDictionary:

    def __init__(self, apiKey):
        self.apiKey = apiKey


    def __textclear(self, text: str):
        text = sub(r'[\r\t\n]', '', text.replace('![CDATA ', '').replace(' ]]>', ''))
        text = text.replace('<![CDATA[', '')
        text = text.replace(']]>', '')
        return text

    
    def search(self, q, **kwargs):
        r"""      
        :param q:           검색어 (str)
        :param method:      검색 방식 (int)
        :param start:       검색의 시작 번호
        :param num:         결과 출력 건수
        :param advanced:    자세히 찾기 여부
        :param target:      찾을 대상
        :param type1:       구분 1
        :param type2:       구분 2
        :param pos:         품사
        :param cat:         전문 분야
        :param multimedia:  멀티미디어
        :param letter_s:    음절 수 시작
        :param letter_e:    음절 수 끝
        :param update_s:    고친 날짜 시작일
        :param update_e:    고친 날짜 종료일
        """

        url = f'https://stdict.korean.go.kr/api/search.do?key={self.apiKey}'


        for k, v in kwargs.items():

            if not k in parameters_search.params:
                raise Exception("이거 파라미터 맞는지 확인좀;;")


            if k == 'method':
                if not v in parameters_search._method:
                    url += f'&{k}=exact'
                else:
                    url += f'&{k}={v}'


            if k == 'start':
                if not v in parameters_search._start:
                    url += f'&{k}=10'
                else:
                    url += f'&{k}={v}'


            if k == 'num':
                if not v in parameters_search._num:
                    url += f'&{k}=10'
                else:
                    url += f'&{k}={v}'


            if k == 'advanced':
                if not v in parameters_search._advanced:
                    url += f'&{k}=n'
                else:
                    url += f'&{k}={v}'


            if k == 'target':
                if not v in parameters_search._target:
                    url += f'&{k}=1'
                else:
                    url += f'&{k}={parameters_search._target[v]}'


            if k == 'type1':
                if not v in parameters_search._type1:
                    url += f'&{k}=all'
                else:
                    url += f'&{k}={parameters_search._type1[v]}'

            
            if k == 'type2':
                if not v in parameters_search._type1:
                    url += f'&{k}=all'
                else:
                    url += f'&{k}={parameters_search._type2[v]}'


            if k == 'pos':
                if not v in parameters_search._pos:
                    url += f'&{k}=0'
                else:
                    url += f'&{k}={parameters_search._pos[v]}'


            if k == 'cat':
                if not v in parameters_search._cat:
                    url += f'&{k}=0'
                else:
                    url += f'&{k}={parameters_search._cat[v]}'


            if k == 'multimedia':
                if not v in parameters_search._multimedia:
                    url += f'&{k}=0'
                else:
                    url += f'&{k}={parameters_search._multimedia[v]}'


            if k in ['letter_s', 'letter_e', 'update_s', 'update_e']:
                url += f'&{k}={v}'



        url += f'&q={q}'
        html = get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        info = {}

        info['total'] = soup.find('total').text
        info['start'] = soup.find('start').text
        info['num']   = soup.find('num').text  

        data = []
        for i in soup.find_all('item'):
            d = {}
            
            d['word'] = self.__textclear(i.find('word').text)
            d['definition'] = self.__textclear(i.find('definition').text)
            d['link'] = self.__textclear(str(i.find('sense')).split('<link/>')[1].split('\n<type>')[0])
            d['type'] = self.__textclear(i.find('type').text)
            d['pos'] = self.__textclear(i.find('pos').text)
            data.append(d)

        info['data'] = data

        return info
