
# 2021-04-05

print('='*50)

'''
import mod1 #mod1.py처럼 확장자까지 모두 쓸필요는없다. 다만 현재 작성중인 파이썬파일과 동일 디랙토리에 있어야만 불러올 수 있다.

print(mod1.add(3,4))
print(mod1.sub(4,2))    #모듈명.함수(입력1,입력2,...etc)의 순서로 입력한다

from mod1 import add    #이런식으로도 불러올수 있다. from 모듈명 import (모듈내)함수
print(add(5,4))

from mod1 import add, sub
from mod1 import *          # *는 해당모듈내 모든 함수를 불러오는 것을 의미한다.

print(sub(6,7))
'''

'''
필요한 모듈이 sys위치에 있지않으며 현재 작성중인 python파일과 동일 디랙토리가 아니라면, sys.path에 추가하는 방식으로 사용가능하다.

>>> python3
>>> import sys
>>> sys.path    ->모듈이있는 sys위치를 path를 통해 리스트값으로 가져온다. 그러므로 이를 이용, append를 사용하여 필요한 모듈위치를 추가.
>>> sys.path.append("users/사용자명/jtp/newfolder")

이제는 항상 가져올 수 있는 sys리스트에 추가했으므로, newfolder에있는 필요한 모듈을 import해서 사용할 수 있게 되었다.

>>> set PYTHONPATH=경로
>>> python
>>> import mod2
>>> print(mod2.add(3,4))
7

이런꼴로도 사용가능하다고는 하는데, 이건 맥이라서 못해봄.
'''

print('='*50)