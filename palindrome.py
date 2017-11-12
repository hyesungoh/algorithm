# 이름 : 오혜성
# 날짜 : 11 12 2017
# 주제 : 문자열에서 가장 긴 회문

def longest_palindrom(s):
    srL = list(s); srL.reverse(); sN = len(srL)
    sR = "".join(srL)
    n = 0; fN = 0; bN = 0;

    while (n < sN) :
        if (sR.count(s[n:sN]) == 1) :
            bN = len(s[n:sN])
            break
        n += 1

    while (sN > 0) :
        if (sR.count(s[0:sN]) == 1) :
            fN = len(s[0:sN])
            break
        sN -= 1

    return max(fN, bN)


s = '저기저사람여보게저기저게보여'
print(longest_palindrom(s))