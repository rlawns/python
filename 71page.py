dog = '개'
animal = '진돗'+ dog
print(animal)

animal ='elephant'
print(len(animal))

animal = 'elephant'
print('총 개수 : ',animal.count('e'))

animal = 'elephant'
print('앞쪽 찾기:', animal.find('e'))
print('ep 찾기:',animal.find('ep'))
print('뒤쪽 찾기:',animal.rfind('e'))
print('위치:', animal.index('e'))
print('el 시작',animal.startswith('el'))

animal='elephant'
print('n이 있다.:','n' in animal)
print('an이 있다.:', 'an' in animal)
print('an이 없다.:', 'an' not in animal)

ai = 'python program'
print('선택 수정:', ai.replace('p','P'))
print('소문자:', ai.lower())
print('대문자:,', ai.upper())
print('swap 대소문자:', ai.swapcase())
print('첫 문자만 대문자:',ai.capitalize())

animal = 'elephant'
animal = animal.upper()
print('전체 대문자 변경 : ', animal)

#Q5.4
seq = 'hello!'
for s in seq:
    print(s)
'''
#Q5.5
import random
pw = str() #pw 이름의 빈 문자열을 생성
chars = '한글우수'
for pw range():
    pw = pw+.choise(chars)
print(pw)
'''

import random
chars=['한','글','우','수']
print(random.choice(chars))

import random
chars=['한','글','우','수']
random.shuffle(chars)
print(chars)
'''
#Q5.6
import random
def passwd(lenght):
    pw =str()
    chars = 'abcdefghiklmnopqrsuvwxyz'+'0123456789'+'!@#$%^&*'
    for pw in range(chars):
        pw = pw + random.choice(chars)
    return chars
print(passwd(8))
'''
'''
price = [1020,870,3160,2650]
fruits = ['사과', '오렌지','포도','복숭아']
print(price)
print(fruits)
'''
'''
price = [1020,870,3160,2650]
fruits = ['사과', '오렌지','포도','복숭아']
print(price[1])
print(fruits[-2])
'''
price = [1020,870,3160,2650]
fruits = ['사과',1020, '오렌지',870,'포도',3160,'복숭아',2650]

a = [3,5,7]
b = a
b[0] = b[0] -2
print('a=',a,'b=',b)

price = [1020,870,3160,365,731]
print(price[0:2])
print(price[0:4:2])
print(price[1:2])

#Q5.7
price = ['사과', '오렌지', '포도','오렌지','복숭아','오렌지']
print(price[1:6:2])

x = 12.23
y = 23.34
packing = [x,y]
type(packing)
print('packing:', packing)
[c1, c2] = packing
print('unpacking\ncl:',c1)
print('c2=',c2)

fruits1 = ['사과', '오렌지','포도']
fruits2 = ['복숭아', '키위']
allfruits = fruits1 + fruits2
print(allfruits)

#Q5.8
student1 = ['민준',173,'서연',168,'현우',171,'민서',189]
student2 = ['동현', 179]
alldata = student1 + student2
print(len(str(alldata) + '개 데이터'))