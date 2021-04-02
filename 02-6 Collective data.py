
# 2021-03-31

#set은 교/합/차집합을 구할때 개꿀임 (25행)

print('='*50)

s1=set([1,2,3])
print(s1)

s2=set('Hello')
print(s2) 

#set은 중복없이 순서를 따지지않고 자료를 만든다. ->순서가 없으면 인덱싱도 할수없다 ㅜ +딕셔너리도 순서가 있는건 아니라서 인덱싱 불가능
#그렇기땜에 인덱싱이 필요하면 리스트or튜플화 해야함

l1=list(s1)
print(l1[1])
print(l1.index(2))

l2=tuple(s2)
print(l2)
print(l2.index("H"))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1&s2) #교집합
print(s1.intersection(s2)) #상동, s1<->s2 O.K.

print(s1|s2) #합집합
print(s1.union(s2)) #상동

print(s1-s2) #차집합
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))

s1=set([1,2,3])
#print(s1.add(4)) -> 이렇게 쓰면 부정문 None이 출력된다. add자체는 수행만 하는것이기때문에 print할 반환대상이 없기때문. 
# 하지만 add작용은 이루어진다. 이는 함수가 내부->외부순서로 수행되기에 add함수가 작용되기때문이다
s1.add(4)   #한개의 값을 추가 list의 append와 비슷
print(s1)

s1.update([5,6,7]) #여러개의 값을 추가 list의 extend와 비슷
print(s1)

s1.remove(1) #측정한 한개의 값을 지운다
print(s1)

print('='*50)