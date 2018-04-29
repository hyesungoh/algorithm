# 이름 : 오혜성
# 날짜 : 04 29 2018
# 주제 : ROT 13

def ROT13(n):
    r = ord(n)
    if (65 <= r and r <= 90):
        if (r + 13 > 90):
            r = 64 + (r + 13 - 90)
        else: r += 13

    elif (97 <= r and r <= 122):
        if (r + 13 > 122):
            r = 96 + (r + 13 - 122)
        else: r += 13

    return chr(r)

s = input()
print(''.join(list(map(ROT13, s))))

# import codecs
# print(codecs.encode(input(), "rot13"))