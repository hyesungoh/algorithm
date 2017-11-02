# 이름 : 오혜성
# 날짜 : 11 02 2017
# 주제 : 2016년의 요일 계산

def getDayName(month, day) :
    dotw = ("FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU")
    beforeDays = 0
    for i in range(1, month) :
        if i == 2 :
            beforeDays += 29
        elif i <= 7 :
            if i % 2 == 1 :
                beforeDays += 31
            else :
                beforeDays += 30
        else :
            if i % 2 == 0 :
                beforeDays += 31
            else :
                beforeDays ++ 30
    beforeDays += (day - 1)
    return dotw[beforeDays % 7]

while (True) :
    insertMonth = int(input("몇월? : "))
    insertDay = int(input("며칠? :"))
    print(insertMonth,"월 ",insertDay,"일은")
    print(getDayName(insertMonth, insertDay), " 입니다")
