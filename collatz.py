# 이름 : 오혜성
# 날짜 : 11 12 2017
# 주제 : 콜라츠 추측

def collatz(num) :
    ans = 0
    while ans < 500 :
        if (num % 2 == 0) :
            num /= 2
        else :
            num *= 3; num += 1

        ans += 1

        if (num == 1) :
            break

    if (ans == 500) :
        return -1

    return ans

print(collatz(6))