N = int(input())
result = []

for n in range(1, N+1):
    numStr = str(n)
    count = 0
    if numStr.find("3") > -1:
        count += numStr.count("3")
    if numStr.find("6") > -1:
        count += numStr.count("6")
    if numStr.find("9") > -1:
        count += numStr.count("9")

    if count == 0:
        result.append(str(n))
    else:
        result.append("-" * count)
print(' '.join(result))