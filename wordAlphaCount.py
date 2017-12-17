# 이름 : 오혜성
# 날짜 : 12 17 2017
# 주제 : 단어에서 제일 많이 포함된 알파벳 출력

s = input().lower()
l = [s.count(chr(i)) for i in range(ord('a'), ord('z')+1)]
print(chr(l.index(max(l)) + ord('A')) if l.count(max(l)) == 1 else '?')