
#2021-03-30

print("="*50)
odd=[1,3,5,7,9]
print(odd)
print(odd[0]+odd[2]+odd[-1])

a = [1, 2, 3, ['a', 'b', 'c']]

print(a[0])
print(a[-1])
print(a[-1][0])
print(a[-1][-1])

a = [1, 2, ['a', 'b', ['Life', 'is']]]

print(a[2][2][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])
a="12345"
print(a[0:2])

a = [1, 2, 3, 4, 5]
print(a[:2])
print(a[2:])

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

a = [1, 2, 3,]
b = [4, 5, 6]
print(a+b)
print(a*3)
print(len(a+b))

c=str(a[1])+"hi"
print(c)
'''
2021-03-31
'''

a=[1,2,3]
a[2]=4
print(a)

del a[1]
print(a)

del a[:]
print(a)

a=[1,2,3]
a.append(5)
print(a)
b=4,5
a.append(b)
print(a)

a.append([5,6])
print(a)

a=[3,2,6,4,1,5]
a.sort()
print(a)

a=['b','a','c']
a.sort()
print(a)

a=['d','a','c','b']
a.reverse() 
print(a)
b=a.index('a') #위치값을 돌려주는것임! (집합a가 뒤집히면 bcab 이기에 a의 위치값은 2가된다)
print(b)


a=[1,2,4]
a.insert(2,3)
print(a)
a.insert(3,9)
print(a)
'''
[1, 2, 3, 4]의 3번째자리(0,1,2,3)에 10을끼워넣는다

자리 0   1   2   3
    1   2   3   4
              ^
              9
->  1   2   3 9 4
즉, 자리위치값이 3이되게끔 끼워넣는다!!
'''

a=[1,2,3,1,2,3]
print(a.remove(3))    #해당하는값의 첫번째 값을 "제거"한다
print(a)

a=[1,2,3]
b=a.pop() #리스트의 맨 마지막요소를 돌려주고, 해당 요소는 삭제
print(a)
print(b)

a=['하하','히히','헤헤','호호','하하','하하','헤히']
b=a.count('하하')
print(a)

a=[1,2,3]
a.extend([4,5])
print(a)

b=[6,7]
b.extend(a[:])
b.sort()
print(b)

c=[8,9]
c+=b[:] # '+='는 extend와 동일한 의미를 가진다
c.sort()
print(c)


print("="*50)