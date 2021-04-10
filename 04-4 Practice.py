
# 2021-04-04

print('='*50)

#A1
def is_odd(a):
    if a%2==1:
        print('%d는 홀수입니다.'%a)
    else:
        print('%d는 짝수입니다.'%a)

number=int(input())
is_odd(number)

# is_odd = lambda x: True if x%2==1 else False   ->이걸로는 한줄짜리도 가능



print('-'*50)

#A2
def average(*numbers):
    result=0
    for i in numbers:
        result = i + result
    j=len(numbers)
    print(result/j)

average(1,2,3,4,5,6,7,8,9,10)

print('-'*50)

#A3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2    #여기다가 int(input1)+int(input2)라고 해도된다.
print("두 수의 합은 %s 입니다" % total)

print('-'*50)

#A4
print("1번만 youneedpyton으로 출력되고, 나머지는 you need python으로 출력된다")
        #땡->3번만 you need python으로 출력되며 나머지는 youneedpython 으로 출력된다.

print('-'*50)

#A5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()   #close를 하지않아서 계속 열려있는상태였기에 출력되지 않았다

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
"""
또는 with문을 써서도 가능하다!
with open('test.txt','w') as f1:
    f1.write("Life is short")
with open('test.txt','r') as f2:
    prinr(f2.read())
"""
print('-'*50)



#A6
f=open("Answer04-4.txt",'a')
f.write(input("저장할 내용을 입력하세요: "))            #입력할때마다 줄이 바뀌면 좋긴할텐데
f.write('\n')                                     # 이걸 추가해서 해결!
f.close()

print('-'*50)

#A7
f1=open('test.txt','r')
data=f1.read()
newdata=data.replace('java','python')
f1.close()

f2=open('test.txt', 'w')
f2.write(newdata)
f2.close()




print('='*50)