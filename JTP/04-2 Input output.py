
# 2021-04-02

print('='*50)

#사용자가 입력한 값을 특정 변수에 대입하는 방법

'''
a=input()  #커서를 생성하고 여기에 내가 입력한 값이 a에 할당된다
print(a)
'''


#number=input('숫자를 입력하세요.: ')

print("Feel" "so" "good") #그냥 ''안에 있는것만 ,없이 나열하면 + 의 의미를가진다
print("Feel"+"so"+"good")
print("Feel","so","good") # , = ' '

for i in range(1,11):
    print(i,end=" ")       
print()

'''
end 사용시 이어서 출력된다는 의미는 정확히는 해당 출력값이 그 이후 출력값 앞에 오게끔 하는것임.
앞뒤에 feel so good이 있고, 그사이에 123을 출력하는 행에 end를 걸어버리면 다음과 같아진다.
feel so good 1 2 3 
feel so good (X)

feel so good
1 2 3 feel so good (O)
'''

print('='*50)