
#2021-03-31

print('='*50)

# {Key1:Value1, Key2:Value2, Key3:Value3, ...} 꼴로 만들어진다. key는 비변동만 가능하며, value는 변동/비변동 모두가능


a={1:'hi'}
b={'ab':[1,2,3]}
print(a)
print(b)

a[2]='b' #2라는 키에 'b'라는 값을 가진 항목을 추가
print(a)
a['name']='pey'
a[3]=[1,2,3]
print(a)

del a[1]
print(a)

grade={'pey':10,"julliet":99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a', 2:'b'}
print(a[1]) #caution! 리스트,튜플과 달리 '1'위치의 값을 가져오거나 슬라이싱하는게 아닌, '1'의 key에 해당하는 value를 가져오는것!

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic['name'])

a = {1:'aa', 2:'bb'}
print(a[1]) # 여기서 b가 출력되는데, 이는 key가 중복이기때문에 생기는 문제! 그러므로 key-value간 일대일대응을 해주어야한다

'''
a={[1,2]:"리스트"} ->할당자체가 불가, 이는 리스트가 변동값이기때문
print(a[1,2])
'''
a={(3,4):"튜플"}  #튜플은 고정값이기에 key역할 수행가능
print(a[(3,4)])

a= {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
b=a.keys()  #list반환값이 아닌 dict_XX값으로 돌려준다.(효율문제) 만일 list로써 필요하다면 list(a.keys())를 사용.
print(b)

'''
굳이 list 안써도 for 반복구문은 이용가능하긴함
그러나 dict값으로 사용시, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
'''


for k in a.keys():
    print(k)

c=list(a.keys())
print(c)
c.insert(2,'company')
print(c)


print(a.values())
print(a.items())

print(a)
a.clear()
print(a)

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

b=a.get('name')
print(b)
'''
print(a.get('nokey')) -> None(거짓이라고 생각)값이 나옴. (없는)값을 주세요! 응없어
print(a['nokey']) -> 아예 오류를 발생시킴. (없는)값을 XX하자. 없는데 어케해
'''

print(a.get('foo','그런키는 없습니다')) #foo라는 키가 없으면 '그런키는 없습니다'라는 값이 나오게끔 했음

print('name' in a) #name이라는 키는 있으므로 참 반환
print('company' in a) #company라는 키는 없으므로 거짓 반환

# print(a.index('name')) ->순서없는 자료형이므로 인덱싱 못함




print('='*50)