import heapq

numbers = [1, 2, 3, 4, 5, 6, 7, 8, -56, 43, 10, 3]

print(heapq.nsmallest(3, numbers))
print(heapq.nlargest(3, numbers))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 750, 'price': 115.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['shares'])

print(expensive)

print(cheap)