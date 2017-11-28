# 이름 : 오혜성
# 날짜 : 11 23 2017
# 주제 : 피보나치 수열

def fibonacci(num) :

    # 재귀함수
    # if num == 0 :
    #     return 0
    # elif num == 1 :
    #     return 1
    # else :
    #     return fibonacci(num-1) + fibonacci(num-2)

    # 일반함수
    # answer = [0, 1]
    # for i in range(2, num + 1):
    #     answer.append(answer[i - 1] + answer[i - 2])
    # return answer[-1]

    f1, f2 = 0, 1
    for i in (range(num)):
        f1, f2 = f2, f1 + f2
    return f1

print(fibonacci(3))