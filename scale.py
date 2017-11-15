# 이름 : 오혜성
# 날짜 : 11 15 2017
# 주제 : 문자열 확인 (음계)

s = input(); ans = ""
ans = "ascending" if s == "1 2 3 4 5 6 7 8" else "mixed"; ans = "descending" if s == "8 7 6 5 4 3 2 1" else ans;
print(ans)