# 이름 : 오혜성
# 날짜 : 12 19 2017
# 주제 : 문자열에서 몇개의 크로아티아 알파벳이 있는지 확인

# croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# s = input(); n = 0
# for i in croatiaAlphabet:
#     if i in s:
#         n += s.count(i); s = s.replace(i, '')
# print(n + len(s))

l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input(); n = len(s)
for i in l:
    n -= s.count(i)
print(n)


# 리스트 컴프리헨션
# l = list(filter(lambda x: x in s, croatiaAlphabet))
# [s.replace(i, '') for i in croatiaAlphabet]

# 정규표현식을 사용한 다른 풀이
# import re;print(len(re.findall('dz=|[csz]=|[dc]-|[ln]j|.',input())))

# 다른 풀이
# a=input();c=a.count;print(len(a)-c('-')-c('=')-c('nj')-c('lj')-c('dz='))
