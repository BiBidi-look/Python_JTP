
# 2021-04-01

print('='*50)

#A1. need가 출력된다. X
'''
-> shirt가 출력된다. 
"Life is too short, you need python"
첫 if행 만족x
두번째 elif 만족x
세번째 elif 만족O -> a와 shirt는 다르기때문.
네번째 elif 만족O -> 문장내에 need가 있다
다섯째 elif 만족x
이때, 가장 먼저 만족하는것이 세번째 이므로 shirt가 출력된다
'''

#A2
add=0
number=0
while number<=1000:
    number=number+1  #이거보단 number+=1이 더 간편하다!
    if number%3==0:add=add+number
    else: continue
print(add)

print('-'*50)

#A3
i=0
while True:
    i=i+1
    if i>5: break
    print('*'*i)   #이 간단한걸 ㅅㅂ... 문자에 수를 곱하면 그만큼 반복출력된다

print('-'*50)

#A4
for i in range(1,101):
    print(i)

print('-'*50)

#A5
score=[70,60,55,75,95,90,80,80,85,100]
total=0
print(len(score))
for a in score:
    total=total+a

print(total/(len(score)))
print(total)


print('-'*50)

#A6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)   #이를 리스트 내포로 다시작성
print(result)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)

print('='*50)