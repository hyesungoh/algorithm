# 이름 : 오혜성
# 날짜 : 11 24 2017
# 주제 : 딕셔너리의 키 값을 기준으로 리스트안의 튜플 형식으로 반환

def sort_dictionary(dic):
    '''입력받은 dic의 각 키와 값을 튜플로 만든 다음, 키 값을 기준으로 정렬해서 리스트에 넣으세요. 그 리스트를 return하면 됩니다.'''
    return list(map(lambda x: (x,dic.get(x)), sorted(list(dic.keys()))))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( sort_dictionary( {"김철수":78, "가하나":97, "정진원":88} ))