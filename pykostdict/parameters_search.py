
"""
https://stdict.korean.go.kr/openapi/openApiInfo.do
국립국어원 표준국어대사전 공식 api 기준으로 작성하였습니다.
"""


params = ['method', 'start', 'num', 'advanced', 'target', 'type1', 'type2', 'pos', 'cat', 'multimedia', 'letter_s', 'letter_e', 'update_s', 'update_e']


# 기본값 (exact)
_method = {
    '일치 검색': 'exact',
    '포함 검색': 'include',
    '시작': 'start',
    '끝': 'end',
    '와일드카드 검색': 'wildcard',
}


# 검색의 시작 번호(기본값 1)
_start = list(range(1, 1001))


# 결과 출력 건수 (기본값 10)
_num = list(range(10, 101))


# 자세히 찾기 여부 (기본값 n)
_advanced = ['y', 'n'] 


# 찾을 대상(기본값 1)
_target = {
    '표제어': 1,
    '원어': 2,
    '어원': 3,
    '발음': 4,
    '활용': 5,
    '문형': 6,
    '문법': 7,
    '뜻풀이': 8,
    '용례': 9,
    '용례 출전': 10,
    '용례 번역': 11,
}


# 구분 1(기본값 all)
_type1 = {
    '전체': 'all',
    '어휘': 'word',
    '구': 'phrase',
    '관용구': 'idiom',
    '속담': 'proverb',
}


# 구분 2(기본값 all)
_type2 = {
    '전체': 'all',
    '고유어': 'native',
    '한자어': 'chinese',
    '외래어': 'loanword',
    '혼종어': 'hybrid',
}


# 품사(기본값 0)
_pos = {
    '전체': 0,
    '명사': 1,
    '대명사': 2,
    '수사': 3,
    '조사': 4,
    '동사': 5,
    '형용사': 6,
    '관형사': 7,
    '부사': 8,
    '감탄사': 9,
    '접사': 10,
    '의존명사': 11,
    '보조 동사': 12,
    '보조 형용사': 13,
    '어미': 14,
    '품사 없음': 15,
}


# 전문 분야(기본값 0)
_cat = {
    '전체': 0,
    '언어': 1,
    '문학': 2,
    '역사': 3,
    '철학': 4,
    '교육': 5,
    '민속': 6,
    '인문 일반': 7,
    '법률': 8,
    '군사': 9,
    '경영': 10,
    '경제': 11,
    '복지': 12,
    '정치': 13,
    '매체': 14,
    '행정': 15,
    '심리': 16,
    '사회 일반': 17,
    '지구': 18,
    '지리': 19,
    '해양': 20,
    '천문': 21,
    '환경': 22,
    '생명': 23,
    '동물': 24,
    '식물': 25,
    '천연자원': 26,
    '수학': 27,
    '물리': 28,
    '화학': 29,
    '자연 일반': 30,
    '농업': 31,
    '수산업': 32,
    '임업': 33,
    '광업': 34,
    '공업': 35,
    '서비스업': 36,
    '산업 일반': 37,
    '의학': 38,
    '약학': 39,
    '한의': 40,
    '수의': 41,
    '식품': 42,
    '보건 일반': 43,
    '건설': 44,
    '교통': 45,
    '기계': 46,
    '전기 전자': 47,
    '재료': 48,
    '정보 통신': 49,
    '공학 일반': 50,
    '체육': 51,
    '연기': 52,
    '영상': 53,
    '무용': 54,
    '음악': 55,
    '미술': 56,
    '복식': 57,
    '공예': 58,
    '예체능 일반': 59,
    '가톨릭': 60,
    '기독교': 61,
    '불교': 62,
    '종교 일반': 63,
    '인명': 64,
    '지명': 65,
    '책명': 66,
    '고유명 일반': 67,
}


# 멀티미디어(기본값 0)
_multimedia = {
    '전체': 0,
    '사진': 1,
    '삽화': 2,
    '동영상': 3,
    '애니메이션': 4,
    '소리': 5,
    '없음': 6,
}


# 음절수 시작(기본값 1)
_letter_s = 1


# 음절수 끝(기본값 1)
_letter_e = 1


# 고친 날짜 시작일
_update_s = None


# 고친 날자 종료일
_update_e = None


