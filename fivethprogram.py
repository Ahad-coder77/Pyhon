#user input.

val=int(input("enter no : "))
print(type(val),val)


name = str (input( "name : "))
age =  int(input("age : "))
marks = float( input("marks : "))

print("wellcome ", name)
print("your age is ", age)
print("your marks : ", marks)


# prectice

num1 =int(input("Enter first no : "))
num2 = int( input("Enter second no : "))

sum=num1 + num2
print("your sum of ",num1," and ",num2, "is = ",sum)

#prectic2

val=float(input("Enter area of square : "))

print("Area of square is = ", val*val)

#prectic 3

a= float(input("Enter first no : "))
b= float(input("Enter second no : "))

print("Average of these two numbers is = ",(a+b)/2)

#prectice 4

a= int(input("a: "))
b=int(input("b: "))

print("true") if a>=b else print("false")

a= int(input("Enter first no: "))
b= int(input("Enter second no : "))
print(a," is greater than ",b) if a>b else print(a, " is less then ", b)