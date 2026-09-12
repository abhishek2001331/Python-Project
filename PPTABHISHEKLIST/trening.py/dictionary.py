# def methodName():
#     print("this is my method")
#     methodName()

# def myName(name):
#         print(name)
# myName("Abhishek")

#even odd number
def num(num):
    if num%2==0:
        print("even")
    else:
        print("odd")    
num(6)        

#factorial of number

def fact(n):
    fact = 1
    for i in range(2,n+1):
      fact = fact*i
      print(fact)
fact(5)

def arithimatic(a , b):
    x = a+b
    print(x)
    y = a-b
    print(y)
arithimatic(6,3)    