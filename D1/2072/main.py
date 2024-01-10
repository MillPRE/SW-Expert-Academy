# 제약 사항
# 각 수 0 <= x <= 10000

# 문제
# 10개의 수를 입력받아 그 중에서 홀수만 더한 값을 출력

# 입력
# 가장 첫 줄에는 테스트 케이스의 개수 T
# 다음 줄 부터 각 테스트 케이스 주어짐
# 테스트 케이스 줄에는 10개의 수가 주어짐

# 출력
# 출력의 각 줄 '#t 정답'
# t는 테스트 케이스의 번호

# ex
# input
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1

# output
# #1 200
# #2 208
# #3 121

# 2
T = int(input())
for t in range(1, T+1):
    num_list = list(map(int, input().split()))
    total = 0
    for n in num_list:
        if n % 2 != 0:
            total += n

    print(f'#{t} {total}')

# 1
# T = int(input())
# answer = []
# for test_case in range(1, T + 1):
#     result = 0
#
#     data = list(map(int, input().split()))
#     for i in range(len(data)):
#         if (data[i] % 2 != 0):
#             result += data[i]
#     answer.append(result)
#
# for i in range(len(answer)):
#     print(f'#{i + 1} {answer[i]}')
