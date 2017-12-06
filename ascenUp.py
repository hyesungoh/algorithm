# 이름 : 오혜성
# 날짜 : 12 06 2017
# 주제 : 정렬 여부 검사

numList = [int(i) for i in input().split()]
sortedList = sorted(numList)
ans = "A" if sortedList == numList else "M"
ans = "D" if list(reversed(sortedList)) == numList else ans
print(ans)

# print(numList)
# print(sortedList)
# print(list(reversed(sortedList)))