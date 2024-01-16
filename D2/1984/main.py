T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    arr = arr[1:len(arr)-1]
    print(f"#{i} {round(sum(arr)/len(arr))}")

