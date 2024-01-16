T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    # create map
    for n in range(N):
        arr.append(list(map(int, input().split())))
    result = []
    # 0 ~ N-1
    for i in range(N-M+1):
        for j in range(N-M+1):
            mSum = 0
            for mi in range(i, i+M):
                for mj in range(j, j+M):
                    mSum += arr[mi][mj]
            result.append(mSum)


    print(f"#{t} {max(result)}")