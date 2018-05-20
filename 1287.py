# 이름 : 오혜성
# 날짜 : 05 21 2018
# 주제 : 문자열 사직연산

# s = input()
# try:
#     print(eval(s))
# except:
#     print("ROCK")

s = input()
try:
    eval(s.replace("+","&").replace("-","&").replace("/","&").replace("*","&"))
    print(int(eval(s.replace("/","//"))))
except:
    print("ROCK")