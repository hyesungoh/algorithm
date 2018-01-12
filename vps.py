# 이름 : 오혜성
# 날짜 : 01 07 2018
# 주제 : 완벽한 괄호

# def is_pair(s):
#     returnBool = False
#     openNum = 0; closeNum = 0
#     for i in s :
#         if i == "(": openNum += 1
#         elif i == ")":
#             closeNum += 1
#             returnBool = openNum == closeNum
#     return "YES" if returnBool else "NO"
#
# [print(is_pair(input())) for _ in range(int(input()))]

# for _ in range(int(input())):
#     returnBool = True
#     openNum = 0; closeNum = 0; s = input()
#     for i in s:
#         if i == "(":
#             if not returnBool: break
#             openNum += 1
#         elif i == ")":
#             closeNum += 1
#             returnBool = openNum == closeNum
#         else:
#             returnBool = False
#             break
#     print("YES") if returnBool else print("NO")


for _ in range(int(input())):
    s = input()
    while s.count("()"): s = s.replace("()", "")
    print("NO" if s else "YES")