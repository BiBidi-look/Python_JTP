
# 2021-04-01

print('='*50)

treehit=0
while treehit<10:
    treehit=treehit+1
    print('나무를 %d번찍었습니다' %treehit)
    if treehit==10:
        print('나무넘어갑니다')

'''
prompt="""
    1.Add
    2.Del
    3.List
    4.Quit

    Enter number: """

number=0
while number !=4:
    print(prompt)
    number=int(input())  #int(input())은 입력값을 대입하는내장함수
'''

'''
coffee=10
money=300
while money:
    print("돈을 받았습니다. 커피를 드리겠습니다.")
    coffee=coffee-1
    print("남은 커피의 갯수는 %d개 입니다."%coffee)
    if coffee==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''

#coffee machine

'''
coffee=10
while True:
    money=int(input("돈을 주세요:"))
    if money==300:
        print("돈을받았습니다. 커피를 드리겠습니다.")
        coffee=coffee-1
    elif money>300:
        print("돈을받았습니다. 커피와 거스름돈 %d을 드리겠습니다."%(money-300))
        coffee=coffee-1
    else:
        print("거지새끼에게 줄 커피는 없습니다.")
        print("아직 커피가 %d개남았으니 돈을가져오십쇼."%(coffee))
    if coffee==0:
        print("커피가 다 떨어져서 영업을 중지합니다.")
        break
'''

a=0
while a<10:
    a=a+1
    if a%2==0: continue
    print(a)

'''
while True:
    print("무한의 인피니티")
'''








print('='*50)