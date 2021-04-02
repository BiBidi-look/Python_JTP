
# 2021-04-02

print('='*50)

'''
f=open("newfile.txt",'w') #open은 내장함수로써 파일이름과 파일열기모드를 input하여, 파일객체를 output한다.
f.close()
'''

''' 
r:읽기모드(읽기만) w:쓰기모드 a:추가모드(파일의 마지막에 새로운내용 추가시 사용)
w는 파일이 존재할경우 원래 내용이 모두사라지며, 없다면 새로만든다.

'''

f=open("/Users/jeong-gyeonghun/Desktop/doitvs/newfolder/newfile.txt",'w')
f.close


f=open('newfile.txt','w')
for i in range(1,11):
    data="%d번째줄입니다.\n" % i
    f.write(data)
f.close


f = open("/Users/jeong-gyeonghun/Desktop/doitvs/newfile.txt", 'r')
while True:
    line = f.readline()
    if not line:break
    print(line,end='')
f.close()


print('동기화를 해보았다.')



print('='*50)