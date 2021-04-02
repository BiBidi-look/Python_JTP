
# 2021-03-31

#문제:https://wikidocs.net/42526

print('='*50)

#A1
print('A1')
a=80
b=75
c=55
d=(a+b+c)/3
print(d)

print('-'*50)

#A2
print('A2')
a=13
b=a%2
print(b)

print('-'*50)

#A3
print('A3')
a="881120-1068234"
year=a[:2]
month=a[2:4]
date=a[4:6]
pin=a[7:]
print(year,month,date,pin)

print('-'*50)

#A4
print('A4')
pin="881120-1068234"
a=pin[7]
print(a)


print('-'*50)

#A5
print('A5')
a="a:b:c:d"
b=a.replace(':','#')
print(b)

print('-'*50)

#A6
print('A6')
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

print('-'*50)

#A7
print('A7')
a=' '.join(['Life', 'is', 'too', 'short'])
print(a)

print('-'*50)

#A8
print('A8')
t1=(1,2,3)
t2=(4,)
t3=t1+t2
print(t3)

print('-'*50)

#A9   ->오답
print('A9')
print(2,"a[('a',)]의 ('a',)는 튜터이기 때문에 값을 바꿀수없다.")

'''
a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python'
a[250] = 'python'

각각수행시 3번째만 안된다.
'name'은 문자고정값
('a',)은 튜플로써 고정값
250은 숫자 고정값을 가지기 때문에 key로써 쓸수있지만

[1]은 list값으로써 비고정값을 가지기때문에 key로써 쓸수없어 오류가 발생한다

'''

print('-'*50)

#A10
print('A10')
a = {'A':90, 'B':80, 'C':70}
b=a.pop('B')
print(b)

print('-'*50)

#A11 ->오답
print('A11')
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a1=set(a[:]) #a1=set(a)로해도 같은결과가 나옴
b=list(a1) #이걸 빠뜨렸음. 운이좋게도 list없이 무작위로 배치된 값이 순서대로 나왔지만, list화를 해야 안정적인 순서로 출력된다
print(a1)

print('-'*50)

#A12
print('A12')
a = b = [1, 2, 3]
a[1] = 4
print(b)
print('이유:a의 데이터와 b의 데이터가 같은 위치에 저장되어있기 때문에, \n변수 a를 통해서 데이터값을 바꾸면 b도 영향이 가서 [1,4,3]으로 출력된다')

print('-'*50)