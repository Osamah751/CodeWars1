# n = int(input("enter the number you want to test"))
n=84
while n < 1000:
    n += 5

while n >= 1000:
    n -= 3

print(n)

n=998
def function(n):
    if n >= 1000:
        return n-3
    else:
        return function(function(n+5))

print(function(84))