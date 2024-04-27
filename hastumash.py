number = list(map(int, input().split()))

shifted_number = [number[-1]] + number[:-1]

print(*shifted_number)

