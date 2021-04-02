multiline='''
life is short
You need python
'''
print(multiline)

head="python"
tail=" is fun!!"
print(head+tail)
print(head*2)

a="life is short"
print(len(a))

print("")

a="life is too short, you need python"
print(a[0],a[12],a[-2])

print("")

b=a[0]+a[1]+a[2]+a[3]
c=a[0:4]
d=a[5:7]
e=a[19:]
f=a[:]
print(b,c,d,e,f)
print("")
g=a[19:-7]
print(g)

print("")

a="20010331Rainy"
year=a[:4]
month=a[4:6]
day=a[6:8]
weather=a[8:]
print(year)
print(month)
print(day)
print(weather)

print("")

a="pythan"
b=a[:4]
c="o"
d=a[5:]
e=b+c+d
print(e)

