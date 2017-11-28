# 이름 : 오혜성
# 날짜 : 11 28 2017
# 주제 : 문자열 속 연속적으로 나타나는 아이템이 제거된 배열 반환

def no_continuous(s):
    if len(s) == 0:
        return []
    l = list(s[0]) + list(map(lambda x: s[x-1] != s[x] and s[x], range(1, len(s))))
    return list(filter(lambda x: x != False, l))

print(no_continuous(""))