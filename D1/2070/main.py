T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    if arr[0] > arr[1]:
        result = ">"
    elif arr[0] == arr[1]:
        result = "="
    else:
        result = "<"
    print(f"#{i} {result}")