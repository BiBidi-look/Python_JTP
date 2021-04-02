
# 2021-03-31

print("="*50)


#bool자료형은 참/거짓을 가리고, 이 두 값만 가진다


a=True
b=False

print(type(a)) #a자료의 자료형을 확인할수있다 -> class 'bool'

print(1==1) # == : 같은지 확인
print(1>2)

'''
    값       |  참 or 거짓
-----------------------
 "python"   |    참
    ""      |    거짓
 [1, 2, 3]  |    참
    []      |    거짓
    ()      |    거짓            -> 걍 없으면 거짓, 있으면 참이라고 생각하면 편하다
    {}      |    거짓
     1      |    참
     0      |    거짓
   None     |    거짓
'''

a=[1,2,3,4]
while a:      #참 조건동안 계속 반복, 거짓이 되면 중지
    print(a.pop())
    print(a[:])

if []:
    print("참")
else:
    print("거짓")


print(bool("python"))
print(bool(""))




print("="*50)