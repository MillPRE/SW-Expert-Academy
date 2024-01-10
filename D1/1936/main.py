# 1 가위
# 2 바위
# 3 보

# 1 2 -> 2 win
# 1 3 -> 1 win
# 2 3 -> 3 win
A, B = map(int, input().split())

if abs(A-B) == 1:
    if A > B:
        print('A')
    else:
        print('B')
else:
    if A < B:
        print('A')
    else:
        print('B')