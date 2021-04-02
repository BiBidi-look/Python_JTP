
# 2021-03-31

print("="*50)

#C, JAVA등은 변수에 값을 데이터를 할당할때 자료형을 정해야하지만, Python은 알아서 그 데이터에 적합한 자료형을 지정해준다.

a = [ 1, 2, 3 ]
'''
a : 변수 -> 배정된 리스트 형식이 자료가 있는 주소를 가르킨다
[1,2,3] : 리스트 형식의 자료
'''

print(id(a)) #a에 할당된 데이터의 주소

b=a

print(id(b)) #a 주소와 동일. 왜냐? 할당된 변수는 a,b두가지여도 저장된 데이터[1,2,3]이 있는 위치는 같기 때문

print(a is b) #위 내용이 사실이라는것을 증명한다

a.insert(1,4)
print(a)
print(b)

b=a[:]  #a[:]통해 '가져온' [1,4,2,3]이라는 데이터를 b에 할당하는것이기에 데이터 위치가 다르다!
print(id(a))
print(id(b))

del a[1]
print(a)
print(b)

a=[1,2,3]

from copy import copy

b=copy(a) # b=a[:]와 동일기능
print(b is a) 

a,b='python','Life' #튜플을 통해서 배정한것이므로 괄호()가 있어도, 없어도된다

print(a)
print(b)

a=b='python' #도 가능

a,b=3,5
a,b=b,a #a와 b의 값을 바꾼다 좌항은 바꿀려는 목적, 우항은 상단행까지 저장되어있는 데이터를 의미
print(a)
print(b)




print("="*50)