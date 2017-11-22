# 이름 : 오혜성
# 날짜 : 11 22 2017
# 주제 : 입력받은 숫자 사이의 소수의 개수, 에라토스테네스의 체 알고리즘 사용

def numberOfPrime(num) :
    sieve = {}
    for i in range(2, num + 1):
        sieve[i] = 0

    for i in range(2, num + 1):
        if sieve[i] == 0:
            n = 2
            while i * n <= num:
                sieve[i * n] = 1
                n += 1

    r = list(map(lambda x : sieve[x] == 0 , sieve))
    return r.count(True)


print(numberOfPrime(10))