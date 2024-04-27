
numbers = list(map(int, input().split()))


bar_numbers = [numbers[-1]] + numbers[:-1]

print(*bar_numbers)

