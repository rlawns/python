#조건문
'''
grade=80
if(grade>=80):
    print('합격입니다.')
'''
'''
#Q.3.1
grade = 50
if(grade>=80):
    print('합격입니다.\n')
else:
    print('불합격입니다.')
'''
'''
my_age = 25
election_age = 18
if(my_age >= election_age): #간격을 띄울때는 t, 한줄 밑에 N
    print(my_age-election_age,'살 넘음','\t투표가능') 
else:
    print(election_age-my_age, "살이 부족",'\t투표불가능')
'''

num=-1
if(num>0):
    print('양수')
elif (num<0):
    print('음수')
else :
    print('0')

for i in range(6,-1,-2):
    print(i)

#Q3.2
for i in range(7,3,2):
    print(i)

sum=0
for i in range(1,11):
    sum += i
    print(i)
print('합계:', sum)
'''
#Q3.3
import time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
    if(i==1):
        print('fire')
'''
for i in range(3):
    for j in range(3):
        print('$')

for i in range(1,10):
    print('[',i, '단 ]')
    for j in range(1,10):
        print(i,'*', j ,'=',i*j)
    print()


for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

sum = 0
for i in range(150):
    if(sum>150):
        continue # 잘사용 안함 
    sum += i
print('sum=',sum, 'i=',i)