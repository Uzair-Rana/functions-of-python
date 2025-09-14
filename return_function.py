def calculate(num1, num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    div = num1/num2
    return add, sub, mul, div


a, b, c, d = calculate(10, 12)
print("the sum of two numbers is:", a)
print("the subtraction of two numbers is:", b)
print("the multiplycation of two numbers is:", c)
print("the division of two numbers is:", d)


def Calculate(a, b):
    print("sum of numbers is: ", a+b)
    print("subtraction of numbers is: ", a-b)
    print("multiplication of numbers is: ", a*b)
    print("division of numbers is: ", a/b)


Calculate(10, 20)
11
