numbers = list(map(int, input().split()))

k = int(input())

if 0 <= k < len(numbers):
    numbers.pop(k)


print(*numbers)
