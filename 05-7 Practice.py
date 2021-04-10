
# 2021-04-07

print('='*50)

#A1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value = self.value - val #self.value -= val로도 대체가능
    
cal=UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

print('-'*50)

#A2
#상속받아야하는 Class-calculator는 동일하기에 입력 생략
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value>=100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

print('-'*50)

#A3
'''
1번 : abs(-3)-3 = 3(-3의 절대값)-3 = 0. -> all([1,2,0])과 같은데, false값에 해당하는 0이 존재하므로 False결과를 반환한다
2번 : 'a'의 아스키 코드값 97을 ord를 통해 얻고, 이를 다시 chr에 입력했기에 원래의 값 'a'가 출력되므로 True결과를 반환한다
'''

#A4
print(list(filter(lambda i:i>0,[1,-2,3,-5,8,-3])))

print('-'*50)

#A5
print(int(0xea)) #int('0xea',16)이 정확하다

print('-'*50)

#A6
print(list(map(lambda a:a*3,[1,2,3,4])))
print('-'*50)

#A7
a=[-8,2,7,5,-3,5,0,1]
print(max(a)+min(a))
print('-'*50)

#A8
print(round(17/3,4))
print('-'*50)

#A9 -> pass

#A10

#A11

#A12
import time
#print(time.strftime('%c', time.localtime(time.time()))) ->오답

print(time.strftime("%Y/%m/%d %H:%M:%S"))  #연/월/일 시:분:초 로 출력된다

print('-'*50)

#A13
import random

data = list(range(1,46))

def random_lotto(data):
    number = random.randint(0,len(data)-1) #이거도 엄연히는 틀림 실제 뽑는값!=위치값이므로 동일한 값을 뽑지않음 choice나 sample로 수정
    return data.pop(number)

result=[]
while len(result)<6:
    result.append(random_lotto(data))

print(result)


#아래 답이 훨씬 짧고 깔끔하긴함.
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
    if num not in result:         # 뽑은 수가 result에 없다면 추가해라! (pop과는 다른방법)-> 엄연히는 다른데..
                                  # 과정은다르지만, 확률상으로는 같다. 그리고 과정상에 시간소모도가 일장일단이 있다.
                                  # 위에서 pop방식자체가 리스트에서 자리를 하나씩 밀어줘야하는데에서 시간소모가 있음 // 아래는 중복일때 반복수행을 해야하므로 시간소모가 있음
        result.append(num)
print(result)

print('-'*50)
'''
import random
def random_pop(data):
    number = random.randint(1,45)      ->(1,45)라고 하면 가끔 오류가 난다. 왜냐면 pop메서드는 index data를 기반으로 수행되기에 
                                         0번째 위치, 11번째위치, 44번째 위치의 list에서 제거하는 방식이므로 0~마지막자리 위치값을 주어야한다.
                                         그렇기에 1~45라고할시, range(1,46)의 리스트에서는 45'번째' 위치가 존재하지 않기에
                                         randint에서 45를 뽑았을때 오류가 발생하는 것이다.
                                         숫자로 작성하려면 0~44 또는 위처럼 0,len(data)-1로써 그 구간을 정해주어야한다.
    return data.pop(number)

data = list(range(1,46))
while len(data)>=40: 
    print(random_pop(data))
'''

print('='*50)