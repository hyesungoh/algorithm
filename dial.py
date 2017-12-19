# 이름 : 오혜성
# 날짜 : 12 19 2017
# 주제 : 문자입력 > 숫자로 해석 > 다이얼 전화기 총 걸리는 시간

dialList = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
            ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

time = 0
for i in list(input()):
    for j in range(len(dialList)):
        if i in dialList[j]:
            time += (j+3)
            break

print(time)

# 다른 풀이
# print(sum(min(ord(c)-64,25)*28//89+3for c in input()))