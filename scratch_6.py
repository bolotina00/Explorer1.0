str = input()
i = 0
s = 0
while str[s] != '0':
    if str[s] == ' ':
        i = i+0
        s = s+1
    else:
        i = i+1
        s = s+1
print(i)