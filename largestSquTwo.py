# 이름 : 오혜성
# 날짜 : 11 21 2017
# 주제 : O과 X로 이루어진 이차원 배열에서 O로 이루어진 정사각형의 최대 넓이

def findLargestSquare(board) :
    """
    :param board: 1와 0로 이루어진 2차원 배열
    :return: 1으로 이루어진 제일 큰 정사각형의 넓이
    """
    returnNum = 0           # 제일 큰 정사각형의 넓이
    vert = len(board)       # 세로 크기
    hori = len(board[0])    # 가로 크기
    realBoard = []
    # O을 1로 X를 0으로 전환
    for i in range(vert) :
        realBoard.append(list(map(lambda x: 1 if x == 'O' else 0, board[i])))

    # 1부터 끝까지 반복
    for y in range(1, vert) :
        # 1부터 끝까지 반복
        for x in range(1, hori) :
            # 현재 반복을 돌고 있는 리스트의 요소가 1일 때
            if (realBoard[y][x] == 1) :
                # 왼쪽, 위쪽, 왼위 대각선쪽 요소들 중 제일 작은 값 + 1을 현재 요소에 저장
                realBoard[y][x] = min(realBoard[y-1][x], realBoard[y][x-1], realBoard[y-1][x-1]) + 1
                # 현재 요소와 제일 큰 정사각형의 넓이 중 큰 것을 저장
                returnNum = max(realBoard[y][x], returnNum)

    # 넓이를 반환
    return returnNum * returnNum


sample = [
    ['X', 'O', 'X', 'O', 'O'],
    ['O', 'O', 'X', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']
]

print(findLargestSquare(sample))