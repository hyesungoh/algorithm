# 이름 : 오혜성
# 날짜 : 01 04 2018
# 주제 : 단어들을 길이, 사전순으로 정렬

s = set()
[s.add(input()) for _ in range(int(input()))]
[print(i) for i in sorted(s, key=lambda n: (len(n), n))]