# 이름 : 오혜성
# 날짜 : 11 24 2017
# 주제 : 문자열들의 n번째 기준으로 정렬

def strange_sort(strings, n):
    return sorted(strings, key=lambda str: str[n])

print( strange_sort(["sun", "bed", "car"], 1) )