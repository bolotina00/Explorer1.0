str = input()
l = len(str)
l= l//3
n = 2
for i in range(l):
    print(str[n], '-', n)
    n = n+3
