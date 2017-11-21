# 이름 : 오혜성
# 주제 : 백준 알고리즘 스택
# 날찌 : 11 21 2017

stackList = []; orderNum = int(input())
for i in range(orderNum) :
    s = input()
    if (s == 'pop') :
        if stackList == [] :
            print(-1)
        else :
            print(stackList[len(stackList)-1])
            del stackList[len(stackList)-1]

    elif (s == 'top') :
        if stackList == [] :
            print(-1)
        else :
            print(stackList[len(stackList)-1])

    elif (s == 'size') :
        print(len(stackList))

    elif (s == 'empty') :
        if stackList == [] :
            print(1)
        else :
            print(0)

    else :
        s = s.split()
        stackList.append(int(s[1]))