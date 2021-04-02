print("="*50)
a="i eat %d apples." %3
print(a)

a="i eat %s apples." %"five"
print(a)

number=10
day="three"
a="i ate %d apples, so i was sick %s days." %(number,day)
print(a)

a="i have %s apples" %3
print(a)
b="rate is %s" %3.234
print(b)

a="Error is %d%%" %98
print(a)

a="%10s" %"hi"
print(a)

'''-는 왼쪽정렬, +는 오른쪽정렬, n개의 칸에 "문자"를 한개씩 배열하고 남은것을 빈칸화'''
say="hi"
person="jane"
a="%-10sjane" %"hi" '''10칸+jane에서 10칸중 좌1(h),좌2(i)에 배열하고 빈칸 8칸을 둔후, jane을 이어서 출력'''
print(a)
b="%-7s%7s" %(say,person)
print(b)

a="%10.4f" %3.42134234
print(a)

number=5
day=3
a="I ate {0} apples. so i was sick {1} days." .format(number,day)
print(a)

a="I ate {number} apples. so i was sick {day} days." .format(number=6,day=4)
print(a)

a="I eat {0} apples. so i was sick {day} days." .format(7,day=5)
print(a)

'''왼쪽정렬은>, 오른쪽정렬은<, 가운데정렬은 ^'''
a="{0:>10}".format("hi")
b="{0:<10}".format("hi")
c="{0:^10}".format("hi")
print(a)
print(b)
print(c)
d="{0:!<10}".format("hi")
print(d)

y=3.42134234
a="{0:0.4f}".format(y)
print(a)
b="{0:10.4f}".format(y)
print(a)
print(b)

a="{{ and }}".format()
print(a)

name='hong9'
age=28
ability='중졸'
a=f'내 이름은 {name}입니다. 나이는 {age}입니다. 그리고 {ability}입니다.'.format(name,age,ability)
print(a)
b=f'내년이면 {age+1}살이된다'
print(b)



d = {'name':'홍구', 'age':30, 'ability':'중졸'}
a=f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}이며, {d["ability"]}입니다.'
print(a)




a=f'{"hi":^10}'
print(a)
b=f'{"hi":=^10}'
print(b)

y=3.42134234
a=f'{y:10.4}'
print(a)

a="hobby"
b=a.count("b")
print(b)

a = "Python is the best choice"
b=a.find('b')
c=a.find('k')
print(b,c)


a = "Life is too short"
b=a.index('i')
print(b)

a=",".join(['a','b','c','d'])
print(a)

a="   o   Hi   o   "
b=a.upper()
print(b)

c=b.lower()
print(c)

d=a.rstrip()
e=a.lstrip()
f=a.strip()
print(d)
print(e)
print(f)

a = "Life is too short"
b=a.replace("Life", "leg")
print(b)    

a = "Life is too short"
b=a.split()
print(b)
c="a:b:c:d"
d=c.split(":")
print(d)


print

print("="*50)