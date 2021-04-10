
# 2021-04-06

print('='*50)

#패키지는 '.'을 이용해서 모듈을 디랙토리 개념으로 계층적 정리를 할 수 있게해줌. ex) a.b -> a패키지의 모듈 b


#이거 집에서 윈도우로 해보기->아직 맥에서 어케해야할지 방법을 모르겠음. game 디랙토리하에 있는 모듈을 path에 추가하는걸 못하는중

'''
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo (정상수행)

>>> from game.sound import echo
>>> echo.echo_test()
echo (정상수행)

>>> import game     -> 이렇게하면 game 디랙토리의 모듈, game 디랙토리의 __init__.py에서 정의된 것만 사용가능하기 때문
>>> game.sound.echo.echo_test()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'sound' (에러)

>>> import game.sound.echo.echo_test
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ImportError: No module named echo_test (에러)


'''




'''
__init__.py 파일은 해당 디렉토리가 패키지의 일부임을 알려주는역할임. (식별표 역할?)
패키지에 포함된 디랙토리하에 모듈이있다 한들 이게없으면 패키지에서 인식X
(3.3버전이상부터는 없어도 인식하는데 하위버전 안전성을 고려하면 해주는게 좋긴함)

'''

'''
>>> from game.sound import *
>>> echo.echo_test()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined

이렇게 *를 이용하여 전체를 가져오려할때는, 특정 디랙토리의 __init__.py파일에 __all__변수를 아래와같이 추가해야한다.
# C:/doit/game/sound/__init__.py
__all__ = ['echo']  -> sound디랙토리에서 *를 이용하여 import할경우 여기서 정의된 echo모듈만 import된다는 의미.

만일 from a.b.c import * 일때, c가 모듈명이면 __all__과 상관없이 가져와진다.

'''







print('='*50)