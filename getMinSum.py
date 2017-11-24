# 이름 : 오혜성
# 날짜 : 11 24 2017
# 주제 : 길이가 같은 두 수열을 곱하고 더하며 제일 작은 수 만들기

def getMinSum(a, b) :
    sorted(a); b.reverse()
    return sum(list(map(lambda x, y: x * y, a, b)))

print(getMinSum([1,2],[3,4]))