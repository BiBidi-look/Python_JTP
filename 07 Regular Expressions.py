
# 2021-04-07

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit(): #isdigit은 해당 문자열의 숫자여부를 T/F로 구분해준다.
                                                                          #isalpha는 반대로 문자열의 문자여부를 T/F로 구분한다.
            word = word[:6] + "-" + "*******" #6번째숫자까지를 가져오고 나머지는 -와 *******를 추가해서 반환
        word_result.append(word)              #위에서 만든 문자를 list에 추가.
    result.append(" ".join(word_result))
print("\n".join(result)) #결과물간에 \n을 추가해서 행으로 구분을 해준다.

#아래는 정규식을 사용하여 간편화한것.
import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))



'''
정규문자열에서 문자 클레스 []는 []내의 문자와 매치한다는것을 의미.
[abc]라면 banana는 매칭되지만 iphone과는 매치되지 않는다.
+[a-bA-Z]:모든 알파뱃, [0-9]:숫자
^는 not을 의미하며 [^abc]일시 banana는 매칭되지 않지만, iphone은 매칭된다

\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.
'''