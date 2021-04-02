
# 2021-04-01

'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
'''
print("="*50)

test_list=['one','two','three']
for i in test_list:
    print(i)

a=[(1,2,3),(2,3,4),(3,4,5)]
for (first,middle,last) in a:
    print(first,last)

marks=[90,25,67,45,80] #나중에 tuple에서 {'1번학생:50', ...}꼴로도 해보기
number=0
for mark in marks:
    number=number+1
    if mark >=60:
        print('%d번학생은 %d점으로 합격했습니다.'%(number,mark))
    else:
        print('%d번학생은 %d점으로 뜨겁게합격했습니다.'%(number,mark))

print('-'*50)

marks={'둘리':80,'도우너':30,'길동':64} #tuple&dictionary응용
students_id={'둘리','도우너','길동'}

for a in marks:
    for i in students_id:
        if a==i:
            print('%s학생의 성적을 검사합니다.' %(a))
            score=marks.get('%s'%(a))
            print('%s학생의 성적은 %d점입니다.'%(a,score))
            if score>=60: print('%s학생은 합격입니다.'%(a))
            else : print('%s학생은 뜨거운합격입니다. 공부하세요.'%(a))
            break
    #복잡하니 좀더 다듬어보자

print('-'*50)


marks={'둘리':80,'도우너':30,'길동':64} #tuple&dictionary응용개선(get->items 이용하여 데이터쌍을 이용)
students_id={'둘리','도우너','길동'}

for (name,score) in marks.items():
    for check_target in students_id:
            if name==check_target:
                print('%s학생의 성적을 검사합니다.' %(name))
                print('%s학생의 성적은 %d점입니다.'%(name,score))
                if score>=60: print('%s학생은 합격입니다.'%(name))
                else : print('%s학생은 뜨거운합격입니다. 공부하세요.'%(name))
                break




marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark<60:
        continue
    print("%d번학생 축하합니다. 합격입니다." %number)

a=range(10)
print(a)  #0,1,2,3,4,5,6,7,8,9 총 10개의 숫자 리스트를 가지는 객체를 만들어줌

a=range(1,11)
print(a)  #1,2,3,4,5,6,7,8,9,10 총 10개의 숫자 리스트를 가지는 객체를 만들어줌. 위와 공통점은 맨끝수는 포함되지 않음!(11'미만')

add=0
for i in range(1,11):
    add=add+i
    print(add)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print('%d번학생 축하합니다.합격입니다.' %(number+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ',)
    print()


a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)

a=[1,2,3,4]
result=[num*3 for num in a]
print(result)

a=[1,2,3,4]
result=[num*3 for num in a if num%2==0]
print(result)

'''
[표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n] 꼴로 리스트 내포문을 만들수도 있다.
'''

result=[x*y for x in range(2,10)
            for y in range(1,10)]
print(result)




print("="*50)