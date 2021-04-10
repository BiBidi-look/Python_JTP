
# 2021-04-06

print('='*50)

#내장함수가 뭐가있는지 아는것은 중요하다. 이미 있는 내장함수를 자기가 또 만들겠다고 반복하는 짓은 시간이 아까운짓이기 때문이다.
#내장함수의 장점은 외부 모듈과는 다르게, import 과정없이도 바로 사용할수있다는점이다.

print(abs(-15.2)) #절대값 출력

print(all([1,2,3]))
print(all([1,2,3,0]))
print(all([[],(),""])) #iterable(반복가능자료, list,tuple,text,dictionary등)자료가 모두 참값이면 true, 하나라도 거짓이면 false출력

#any는 all의 반대로써, iterable자료중 하나라도 참이있으면 true, 모두 거짓이어야 false를 출력한다

print(chr(98)) #숫자에따른 ASCII code에 해당하는 문자열 출력   <-> ord()사용시, 해당 문자의 아스키 코드값을 돌려준다

print(dir([1,2,3])) #객체가 자체적으로 가지고 있는 변수, 함수를 모두보여줌

print(divmod(7,3)) #두개의 값을 받아 a/b의 몫, 나머지를 튜플형태로써 반환한다.

for i, name in enumerate(['머리','어깨','무릎','발']): #enumerate는 순서있는 자료(리스트 튜플 문자)를 받아 인덱스 값 포함 객체를 반환
    print(i,name)
    print(type(name))
#기타 내용은 https://wikidocs.net/32 참조

class person : pass

a=person()
b=3
print(isinstance(a,person))
print(isinstance(b,person)) # (인스턴스,클레스명)를 입력받아서 첫번째 인수가 클레스의 인스턴스인지 확인하여 참/거짓을 출력함

def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)                           #A

def two_times2(x): 
    return x*2
print(list(map(two_times2, [1, 2, 3, 4]))) #A의 결과를 map을 이용하여 간단히 했다.
                                           #이처럼 map은 입력받은 자료 각요소를 함수에 맞춰서 수행하고 그결과를 묶어서 돌려준다.
                                           #map은 내장함수로써 타입을 확인해도 'map'으로만 나온다. 그냥 그 결과를 묶은'상태' 라고봐야할듯?
                                           #https://3months.tistory.com/338
                                           #여기서 map이 반환하는것은 실제로는 lterator를 반환한다고 되어있다. 그리고 이를 list로 변환하여 그 자료형으로 만드는것.
                                           #lterator는 list같은 종류보다 상위의 객체로써 이렇게 반환시 가지는장점은 list 뿐만아니라 set 자료구조로써 변환시킬수있는등 여러장점이있다.

print(list(map(lambda a: a*2, [1, 2, 3, 4]))) #lambda를 쓰면 더 간단히도 가능하다!

#open은 w,r,a,b 총 4가지가 있는데, b는 바이너리모드이며 rb, wb이런식으로 쓰임.
#바이너리란 정보형태를 말하며, 아스키모드, 바이너리모드가 있다. 텍스트문자형은 아스키 모드이고, 그이외의 모든 그림,영상형태의 정보들은 바이너리라고 본다
#아무말도없다면 f=open('test.txt') -> 기본값인 'r'로써 열림

#pow(a,b)=a**b

print(list(range(0, -10, -2))) #range인수 3개시 세번째는 숫자간의 거리를 의미한다. (-2구간의 숫자만 출력)

print(round(3.1415,3)) #(a,b)에서 숫자a를 반올림해서 소수 b자리까지 표기.


#sorted([2,1,3]) -> 입력값을 정렬하여 그결과를 리스트로 반환
#sort ->리스트 자료형에서의 sort는 객체 그자레만 정렬하지, 그 결과를 돌려주지는 않음


#zip -> 동일갯수의 자료형을 동일 순서로 맟추어 묶어준다. 아래는 그 예시이다.
'''
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
'''










print('='*50)