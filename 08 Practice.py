
# 2021-04-07

print("="*50)

#A1.
a="a:b:c:d"
b=a.split(':')
c="#".join(b)
print(c)

print('-'*50)

#A2.
a = {'A':90, 'B':80,}
print(a.get('C',70))

print('-'*50)

#A3.
'''
a = [1, 2, 3]
print(id(a))
a = a + [4,5]
print(id(a))

a = [1, 2, 3]
print(id(a))
a.extend([4,5])
print(id(a))

이를 보면알수있다.
+할시, 그결과값을 새로운 객체로써 저장하기에 그 위치가 달라지는데, extend를 사용하면 해당 저장위치에 값을 추가하는형식이라 위치가 변하지 않는다.
'''

#A4.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result=0
for i in A:
    if i>=50:
        result+=i
    else: pass

print(result)

'''풀이 : 리스트에서 하나씩 뽑아내면서 50이상일때 더하고, 리스트내부에 값이 없어져서 False반환시 꺼지게 되어있음.
result = 0
while A:                # A 리스트에 값이 있는 동안
    mark = A.pop()      # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark >= 50:      # 50점 이상의 점수만 더함
        result += mark

print(result)           # 481 출력
'''

print('-'*50)

#A5. 왜 어렵게풀었냐... 문제에서는 그냥 n'번쨰'의 피보나치 수열을 순서대로 내뱉으면 되는데, 나는 정수'n'이하의 피보나치 수열을 내뱉는걸 만들었음.
n=5
result=[0,1]
while result[len(result)-1]<n:
    newdata=int(result[len(result)-2])+int(result[len(result)-1])
    result.append(newdata)
if result[-1]>n:
    print(result[:-1])
else:
    print(result)

'''재귀호출을 이용한 풀이
print('아래는 해설')
def fib(n):
    if n == 0 : return 0          # n이 0일 때는 0을 반환
    if n == 1 : return 1          # n이 1일 때는 1을 반환
    return fib(n-2) + fib(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

for i in range(2):
    print(fib(i))
'''

print('-'*50)

#A6.
'''
data=input("숫자를 입력하세요.:")
list_data=data.split(',')

result=0
i=0
while i<=len(list_data)-1:
    result+=int(list_data[i])
    i+=1
print(result)
'''

'''풀이는 while이 아니라 for 문을 사용했음. 이렇게하면 i를 정의할 필요가없고, while 회전을 위해 i+=1를 쓰지않아도되니 2줄이 줄어든다.
user_input = input("숫자를 입력하세요: ")
numbers = user_input.split(",")
total = 0
for n in numbers:
    total += int(n)    # 입력은 문자열이므로 숫자로 변환해야 한다.
print(total)
'''


print('-'*50)

#A7.
'''
num=input("구구단을 출력할 숫자를 입력하세요(2~9):")
mul=range(1,10)  ->이걸 그냥 for문에 통째로 넣으면 1줄을 줄일수있다.

for i in mul:    -> for i in range(1,10)으로 
    result=int(num)*int(i)
    print(result,end=" ")
print()
'''

print('-'*50)

#A8.
f1=open("abc.txt",'r')
line=f1.readlines()     #줄단위 list형태로 읽어옴.
line.reverse()
del line[0]             #124~127줄에서 \n을 지우고 만드는과정이 비효율적.
line.insert(0,'EEE\n')  #이를 for문에서 line을 한줄씩 쓸때 빈칸을 제거하고, 입력할때마다 \n을 다음줄에 출력하게 하면 굳이 이런짓 안해두댐
del line[4]
line.insert(4,'AAA')
f1.close()

f2=open("abc.txt",'w')
for i in range(0,len(line)):  #range를 이용하지않고 바로 line을 불러오면 효율적.
    data=line[i]
    f2.write(data)
f2.close()

''' #해설 - 내꺼는 비효율끝판왕 ㅋㅋㅋㅋ
f = open('abc.txt', 'r')
lines = f.readlines()    # 모든 라인을 읽음
f.close()
print(type(lines))
lines.reverse()          # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()  # 포함되어 있는 줄 바꿈 문자 제거
    f.write(line)
    f.write('\n')        # 줄 바꿈 문자 삽입
f.close()
'''


#A9.
f=open("sample.txt",'r')
total=0
count=0
while True:
    line=f.readline()    #readlines를 쓰면 줄단위데이터를 list로 반환하기떄문에 while문을 이용한 한줄씩 가져오는 짓을 안해두댐
    count+=1
    if not line : break
    total+=int(line)
average=total/(count-1)
f.close()

w=open("result.txt",'w')
w.write(str(total))     #해설에서는 평균값만 165,166줄은 삭제해도 무방
w.write('\n')
w.write(str(average))
w.close()
'''
f = open("sample.txt")
lines = f.readlines( )  # sample.txt를 줄 단위로 모두 읽는다.
f.close( )

total = 0
for line in lines:
    score = int(line)  # 줄에 적힌 점수를 숫자형으로 변환한다.
    total += score
average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()
'''

#A10.
class Calculator():
    def __init__(self,data):
        self.first=data[0]
        self.second=data[1]
        self.third=data[2]
        self.fourth=data[3]
        self.fifth=data[4]
        print(len(data))
    def sum(self):
        total=self.first+self.second+self.third+self.fourth+self.fifth  
        print(total)
    def avg(self):
        average=(self.first+self.second+self.third+self.fourth+self.fifth)/5
        print(average)

'''풀이 -> 여기서는 1~5를 하나씩 배정하지않고 numberlist로 
class Calculator:
    def __init__(self, numberList): 
        self.numberList = numberList

    def sum(self): 
        result = 0
        for num in self.numberList:  -> 5개를 각각가져오지않고 for문을 이용하여 리스트 하나당 num하나에 대응하도록 만들어서 매우 간략화
            result += num
        return result

    def avg(self):
        total = self.sum()           ->재귀함수화? 를 통해서 sum내용을 가져온다
        return total / len(self.numberList)
'''

cal1=Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2=Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

#A11.
'''
A11-1
>>> import sysx
>>> sys.path.append(C:\doit)

A11-2
++(해설추가) set PYTHONPATH를 이용하여 모듈을 가져옴

A11-3
++ 사용하는 파이선파일을 mymod.py가 있는 위치에서 구동하기.
'''

#A12
'''
result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:  ->첫행 [1,2,3][3]에 의해서 3이 추가된다 : 0+3
    result += 3
finally:            ->진행에 상관없이 무조건 수행되므로 4가 추가된다 : 0+3+4
    result += 4

print(result)       ->7이 출력된다
'''

#A13
'''
def DashInsert(num):
    i=0
    while True:
        try:
            if int(num[i])%2==1 and int(num[i+1])%2==1:
                num = num[:i+1] + '-' + num[i+1:]
                i+=2
                continue
            elif int(num[i])%2==0 and int(num[i+1])%2==0:
                num = num[:i+1] + '*' + num[i+1:]
                i+=2
                continue
            else:
                i+=1 
                continue
        except IndexError:
            print(num)
            break

num=input("숫자입력:")
DashInsert(num)
'''

'''해설
data = "4546793"
numbers = list(map(int, data))   # 숫자 문자열을 숫자 리스트로 변경 (숫자문자열->숫자정수화->숫자리스트화)
result = []

for i, num in enumerate(numbers):   #enumerate -> 순서있는 자료(list)를 index값(i) + 해당list문자값(num) 조합으로 반환
                                    #7의 경우, 4 7 (위치값4, 해당위치 문자7)
    result.append(str(num))         #result 리스트에 위치에따른 숫자문자를 추가
    if i < len(numbers)-1:                   # 다음 수가 있다면
        is_odd = num % 2 == 1                # 현재 수가 홀수(현재 가져온 num데이터)
        is_next_odd = numbers[i+1] % 2 == 1  # 다음 수가 홀수(아직안가져온 리스트의 다음숫자판독)
        if is_odd and is_next_odd:           # 연속 홀수
            result.append("-")
        elif not is_odd and not is_next_odd: # 연속 짝수
            result.append("*")

print("".join(result)) #result리스트를 공백없이 연속으로 출력.
'''

#A14.
#문자열이 반복되지 않을때, 그사이에 구분용 문자를 넣고, 이를 split하여 구분시킨다. 이후 count를 통해 각 항목별 갯수를 세고, 앞글자를 +숫자로 출력

text='aaabbcccccca'

i=0
while 1:
    try:
        if text[i] != text[i+1]:
            text = text[:i+1] + '-' + text[i+1:]
            i+=2
            continue
        else :
            i+=1
            continue
    except IndexError:
            break

text_sep = text.split('-')
count_num=len(text_sep[0])

j=0
while j < len(text_sep):
    count_num=len(text_sep[j])
    print(text_sep[j][0],end='')
    print(count_num,end='')
    j+=1
print()

'''
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:                                #문자열 s(str상태) 앞에서부터 하나씩 c에 배정한다!
        
        if c!=_c:                              #이전에 검사했던글자 c_가 새로가져온글자 c와 다르다면
            _c = c                               #기존의 글자값_c에 새로 가져온 글자 c를 배정한다.

            if cnt: result += str(cnt)               #그리고지금까지 세어온 횟수를 result의 처음 세기시작한 문자 뒤에 기록한다

            result += c                          #결과값에 가져온 글자값 c를 추가한다
            cnt = 1                              #이제 새로운 글자를 처음으로 센것이다.

        else:                                      #이전에 검사했던 글자 c_가 새로가져온 글자c와 같다면 cnt에 횟수를 한번 추가한다.
            cnt +=1 
                                        #앞들의 연산에 의해 더이상 cnt는 0일수가없다.
    if cnt: result += str(cnt)                               #마지막글자를 확인한 후, 마지막 글자의 횟수를 result에 추가한다.
    return result

print (compress_string("aaabbcccccca"))  # a3b2c6a1 출력
'''


#A15. 이건 내꺼가 더 효율적인거같은뎅
def CheckNum(num):
    num_check=list(set(str(num)))
    print(len(num_check) == 10)

num=input('숫자배열을 입력하세요:')
CheckNum(num)

'''
def chkDupNum(s):
    result = []
    for num in s:                #가져온 문자의 앞자리를 하나씩 가져오는데, 
        if num not in result:    #이게 기존의 숫자들을 집어넣은 result리스트에없다면 추가하고
            result.append(num)
        else:                    #있다면 거짓을반환함.
            return False
    return len(result) == 10

print(chkDupNum("0123456789"))      # True 리턴
'''





#16.
morse_code={
    '.-':'A',
    '-...':'B',
    '-.-.':'C',
    '-..':'D',
    '.':'E',
    '..-.':'F',
    '--.':'G',
    '....':'H',
    '..':'I',
    '.---':'J',
    '-.-':'K',
    '.-..':'L',
    '--':'M',
    '-.':'N',
    '---':'O',
    '.--.':'P',
    '--.-':'Q',
    '.-.':'R',
    '...':'S',
    '-':'T',
    '..-':'U',
    '...-':'V',
    '.--':'W',
    '-..-':'X',
    '-.--':'Y',
    '--..':'Z'
    }

morse=".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
morse_sent=morse.split("  ")

i=0
while i < len(morse_sent):
    morse_sent[i]=morse_sent[i].split()
    i+=1

sentance=0
word=0
while sentance<len(morse_sent):
    while word<len(morse_sent[sentance]):
        print(morse_code[morse_sent[sentance][word]],end='')
        word+=1
    print(end=' ')
    word=0
    sentance+=1
print()

'''
dic = {                                                                 #이거 노가다는 똑같음
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):            #가져온 모스 신호를 단어단위로 나누어 list화함
        for char in word.split(" "):            #단어단위로 list화한거를 다시 알파뱃1개단위로 list화 시킴 -> [ [] [] [] ]꼴
            result.append(dic[char])            #알파벳 단위의 모스부호(key)에 해당하는 알파벳(value)값을 result 리스트에 추가
        result.append(" ")                  #단어 하나끝날때마다 공백하나를 집어넣어서 단어구분을함
    return "".join(result)          #마지막으로 result list를 str형태로 반환


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

'''






#A17~20. 정규표현 pass














print('='*50)