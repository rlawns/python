def double(num):
    print(num,'의 제곱:',num*num)
double(3)

def hello():
    print('hello!')
hello()

def double(num):
    return num*num
result = double(3)
print('%d의 제곱: %d' % (3, result))

def double(n):
    square = n*n
    return square
print(double(7))

def add(a,b):
    sum=a+b
    return sum
print(add(3,5))

def add_sb(a,b):
    sum = a+b
    diff = a-b
    return sum, diff
print(add_sb(9,50))

def swap(a,b):
    temp = a
    a = b
    b = temp
a=3
b=5
swap(a,b)
print('a=', a,', b=',b)

def swap(a,b):
    return b,a
a=3
b=5
a,b = swap(a,b)
print('a=', a,', b=',b)

#Q.4.1
def sum(n):
    sum = 0
    for i in range(1,11):
        sum +=i
    return sum
print(sum(10))

def factorial(n):
    result=n*n+1
    for i in range(n):
        result = n*i
    return result
print('3!=', factorial(3))
'''
import turtle
turtle.forward(100)
'''
'''
import turtle
turtle.shape('turtle')
turtle.forward(10000)
'''
'''
import turtle
turtle.forward(100)
turtle.right(90)
'''
'''
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
'''
'''
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
import math
turtle.right(90+45)
turtle.forward(math.sqrt100*100*2)
'''
'''
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.setpos(0,0)
'''
'''
import turtle
turtle.circle(100)
'''
'''
import turtle
turtle.circle(-100)
'''
'''
#Q4.2
import turtle
turtle.forward(100)
turtle.right(45)
turtle.circle(-100)
turtle.right(45)
turtle.forward(100)
turtle.right(90+45)
turtle.setpos(0,0)
'''
'''
import turtle
turtle.circle(50)
turtle.circle(-100)
'''
'''
#Q4.3
import turtle
import random
rad = random.randint(50,100)
turtle.circle(100)
'''
'''
import turtle
import random
col =random.randint(0,3)
if(0 == col):
    turtle.pencolor('yellow')
elif(1 == col):
    turtle.pencolor('blue')
elif(2 == col):
    turtle.pencolor('red')
turtle.circle(50)
'''
'''
import turtle
import random
for i in range(3):
    col=random.randint(0,2)
    sel=random.randint(0,1)
    if(0 == col):
        turtle.pencolor('yellow')
    elif(1 == col):
        turtle.pencolor('blue')
    elif(2 == col):
        turtle.pencolor('red')
    if(0==sel):
        turtle.forward(100)
    elif (1==sel):
        turtle.circle(50)
        turtle.right(45)
'''
'''
import turtle
import random
for i in range(10):
    for j in range(5):
        col = random.randint(0,3)
        if (0 == col):
            turtle.pencolor('yellow')
        elif (1 == col):
            turtle.pencolor('blue')
        elif (2 == col):
            turtle.pencolor('red')
        elif (3 == col):
            turtle.pencolor('green')
        col=random.randint(0,4)
        if(0 == col):
            turtle.color('red')
        elif(1 == col):
            turtle.color('blue')
        elif(2 == col):
            turtle.color('green')
        elif(3 == col):
            turtle.color('purple')
        elif(4 == col):
            turtle.color('yellow')
        sel = random.randint(0,3)
        if(0 == sel):
            turtle.forward(random.randint(50,100))
        elif (1 == sel):
            turtle.right(random.randint(90,360))
        elif (2 == sel):
            turtle.begin_fill
            turtle.circle(random.randint(-100, -20))
        elif (3 == sel):
            turtle.forward(random.randint(30,50))
    a = float(random.randint(-300,300))
    b = float(random.randint(-300,300))
    turtle.goto(a,b)
'''
print("my friend's house.") 
#Q5.1
print("doesn't")

animal = 'frog'
print(animal[2])

animal = 'frog'
print(animal[-1])

animal = '나무늘보'
print(animal[0])
print(animal[-3])
print(animal[2])
print(animal[-1])

#Q5.2
fruit ='오렌지'
print(fruit [1])
print(fruit [-2])

fruit ='오렌지'
print(fruit [1:2])

#Q5.3
animal = 'frog'
print(animal[1:4:2])

animal = 'elephant'
print(animal[1:7:2])

animal = 'elephant'
print(animal[5:])

animal = 'elephant'
print(animal[:3])

animal = 'elephant'
print(animal[3:-3])
'''
animal = 'elephant'
print(animal[:])
'''
animal = 'elephant'
print(animal[-5:5])

animal = 'elephant'
print(animal[::3])
print(animal[::-1])
print(animal[::])
