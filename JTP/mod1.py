#mod1.py for 05-2 Module.py

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
'''
터미널에서 python3 실행, 이후 'import mod1'을 이용하여 모듈을 직접 가져와서 쓸수도있다.
사용하려면 똑같이 print(mod1.add(3,4))꼴로 입력하면 7이 결과값으로 출력된다.
'''
if __name__ == "__main__":      #아래의 문제를 이 행을 사용해서 해결가능하다.           <-ㄱ
    print(add(1,4))                                                             
    print(sub(4,2))         #해당 프린트행 때문에 결과값이 자동으로 터미널창에 출력된다.     -|
                            #이 때문에 위방법을 사용하면 모듈만 가져와서 사용할 수 없다.    

'''
대화형 인터프리터나 다른곳에서 mod1.py를 가져와서 사용시에는, __name__ == "__main__"이 거짓이 되어 출력되지 않는다.
다만 직접 이 파일을 실행하면 참이되어 출력된다.

__name__ 변수란?

파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.


'''



