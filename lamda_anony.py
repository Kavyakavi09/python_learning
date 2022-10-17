# lambda anonymous function
import random
num1=random.randint(1,9)
num2=random.randint(2,8)
x= lambda nu1,nu2: nu1*nu2
print(x(num1,num2))

# lambda adv

def add(num1):
    return lambda num2:num1+num2

res=add(4)
print(res(5))