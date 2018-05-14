# 이름 : 오혜성
# 날짜 : 05 15 2018
# 주제 : 카이사르 암

def caesar(n):
    r = ord(n)
    if (r - 3 < 65):
        r = 90 - (67 - r)
    else:
        r -= 3
    return chr(r)

s = input()
print(''.join(list(map(caesar, s))))