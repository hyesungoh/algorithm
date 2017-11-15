# 이름 : 오혜성
# 날짜 : 11 08 2017
# 주제 : n개의 도시는 위치와 인구를 가지고 있으며 이동거리를 최소화 할 수 있는 도시 선택

def chooseCity(n, city) :
    resultList = [0] * n
    for i in range(0, n) :
        for j in range(0, n) :
            if (i == j) :
                continue
            else :
                distance = city[i][0] - city[j][0] if city[i][0] - city[j][0] > 0 else -1 *(city[i][0] - city[j][0])
                resultList[i] += distance * city[j][1]

    return city[resultList.index(min(resultList))][0]



l = [[1, 5],[2, 2],[3, 3]]
print(chooseCity(3, l))

