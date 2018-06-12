# 이름 : 오혜성
# 날짜 : 06 13 2018
# 주제 : 문장에서 모음의 순서만 뒤바꾸기

vowels = ['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']

def reverseVowel(s):
    l = []
    sL = list(s)
    for w in sL:
        if w in vowels: l.append(w)

    for i in range(len(sL)):
        if sL[i] in vowels: sL[i] = l.pop(len(l)-1)

    return ''.join(sL)

print(reverseVowel(input()))