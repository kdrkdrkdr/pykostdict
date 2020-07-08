# pykostdict
국립국어원 표준국어대사전 파이썬 API

API 서버에 요청하여 검색결과를 가져와 줍니다.


## 사용법
```python
kostdict = KoreanStandardDictionary(apiKey='발급받은 API키')
a = kostdict.search(q="미분", num=12, target='원어', pos='수사')
print(a)

"""
{'total': '4', 'start': '1', 'num': '12', 'data': [{'word': '미분', 'definition': '아직 나뉘지 않음.', 'link': 'https://stdict.korean.go.kr/search/searchView.do?word_no=126058&searchKeywordTo=3', 'type': '일반어', 'pos': '명사'}, {'word': '미분', 'definition': '쌀을 빻은 가루.', 'link': 'https://stdict.korean.go.kr/search/searchView.do?word_no=126060&searchKeywordTo=3', 'type': '일반어', 'pos': '명사'}, {'word': '미분', 'definition': '어떤 함수의 미분 계수를 구하는 일.', 'link': 'https://stdict.korean.go.kr/search/searchView.do?word_no=433885&searchKeywordTo=3', 'type': '일반어', 'pos': '명사'}, {'word': '미분', 'definition': '고운 가루.', 'link': 'https://stdict.korean.go.kr/search/searchView.do?word_no=126062&searchKeywordTo=3', 'type': '일반어', 'pos': '명사'}]}
"""

# KoreanStandardDictionary 인스턴스 하나 만들고 .search(요청변수=허용값) 의 형태로 넣어서 해주시면 됩니다.
```

## 더 많은 매개변수는 국립국어원 API 소개 페이지에서 확인 할 수 있습니다.
https://stdict.korean.go.kr/openapi/openApiInfo.do


## 업데이트
아직 beta 버전입니다.