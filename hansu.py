# 이름 : 오혜성
# 날짜 : 12 10 2017
# 주제 : 1부터 N까지의 한수의 갯수

def isitHansu(num):
    if (num < 100):
        return True
    elif (num == 1000):
        return False
    else:
        numStr = str(num)
        if (int(numStr[0]) - int(numStr[1]) == int(numStr[1]) - int(numStr[2])):
            return True
        else:
            return False

l = list(filter(isitHansu, range(1, int(input())+1)))
print(len(l))

# 다른 사람의 풀이
# print(sum((N//100-N//10%10==N//10%10-N%10)|(N<100)for N in range(1,int(input())+1)))