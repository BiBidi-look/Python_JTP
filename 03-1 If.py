
# 2021-03-31

print('='*50)

money=False
if money:
    print("나는")
    print('부자')
else:
    print('나는거지야')

# 'x != y' = x와 y가 같지 않다. 이거만 잘 생각해두자 나머지는 다 아는얼굴들이다.

x=3
y=2
print(x>y)

money=2000
if money>=3000:
    print('택시타고집가자')
else:
    print('걸어가 거지야')


# 'not x' x가 거짓이면 참이다. 이거만 잘 기억해두자. 나머지는 알구있다구~

money=2000
card=True
if money>=3000 or card:
    print('택시타고집가자')
else:
    print('걸어가 거지야')

# 긍정집합조건 : x in List/Tuple/Text
# 부정집합조건 : x not in List/Tuple/Text

a=[1,2,3]
print(1 in a)
print(4 not in a)

a=('2',)
print(3 in a)
print(2 not in a)

pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시타고간다거지새끼들아")
else:
    print('걸어다니는거지새끼')

if 'money' in pocket:
    pass    #주머니에 돈이있기때문에 그냥 if문을 무시한다. 물론 Else문도 패스한다
else:
    print('걸어다니는거지새끼')

pocket=['paper','handphone']
if 'money' in pocket:
    print('texi')
else:
    if card in pocket:
        print('text')
    else:
        print('꺼져거지야')

pocket=['paper','handphone']
if 'money' in pocket:
    print('texi')
elif 'card' in pocket:
    print('texi')
elif 'handphone' in pocket:
    print('삼성페이')
else:
    print('거지야 꺼져')


pocket=['paper']
if 'money' in pocket:print('texi')
elif 'card' in pocket:print('texi')
elif 'handphone' in pocket:print('삼성페이')
else:print('거지야 꺼져')

score=60
if score<60:print('불합격')
else:print('합격')

message= "합격" if score>=60 else "뜨거운합격"
print(message)

print('='*50)