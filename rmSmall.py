# 이름 : 오혜성
# 날짜 : 11 07 2017
# 주제 : 리스트에서 제일 작은 것 삭제

def rm_small(l) :
    l.pop(l.index(min(l)))
    return l

test = [1,2,3,4]
print(rm_small(test))