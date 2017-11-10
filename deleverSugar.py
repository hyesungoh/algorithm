# 이름 : 오혜성
# 날짜 : 11 10 2017
# 주제 : N 나누기 5, 3 / 최대한 많은 5로 나눈 값

n = int(input())
five = int(n / 5)
for i in range(five,-1,-1) :
    num = n
    num -= (i * 5)
    if (num % 3 == 0) :
        break;

if (i==0 and num%3!=0) :
    print(-1)
else :
    print(int(i+num/3))
