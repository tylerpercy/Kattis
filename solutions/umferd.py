x = int(input())
y = int(input())

cars = 0

for i in range(0, y):
    cars += input().count('#')

print(1 - (cars / (x*y)))