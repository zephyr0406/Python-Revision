print("Hello World")
#Variables
a = 10
b = 15
sum = a + b
c = 2*(a+b)
print(sum)
print(c)

#Arithmetic Operators -- generates mathematical values
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b) #remainder
print(a**b) #a^b

#Relational Operators -- generates boolean values
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Assignment Operators -- Assigns Values to the variables
num = 10
num += 10   # that is equal to num = num + 10 = 10 + 10 = 20
num -= 10   # that is equal to num = num - 10 = 10 - 10 = 0
num *= 10   # that is equal to num = num * 10 = 10 * 10 = 100
num /= 10   # that is equal to num = num / 10 = 10 / 10 = 1
num %= 10   # that is equal to num = num % 10 = 10 % 10 = 0
num **= 10  # that is equal to num = num ** 10 = 10 ** 10 = 10^10

print(num)

#Logical Operators -- Used to create conditions

x = 50
y = 30
print(not (x>y))  #not operator gives the opposite of the generated boolean value
print(not (x<y))  #should be false here but not operator changed it to true, whatever you give it, it makes it opposite

val1 = False
val2 = True
print(val1 and val2) #used to check if the two values are true or not, if any value is false it gives the output as false

print(val1 or val2) #used to check if any of the two values are true or not


#Type Conversion

ax = 2
by = 3.6
cz = ax + by # here 'ax' is an integer and 'by' is a float so 'ax' is automatically converted into a float to do the addition
print(cz)

#Type Casting

d = "2"
e = 8.5
f = int(d)
print(e + f)


#Input Statements

a = input("Enter your Name")
b = input("Enter your favourite color")
print("welcome " + a, "your favourite color is", b)

#Practice Questions

#Q1 write a program to input for two numbers and print their sum

#Ans-
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum of the given numbers is", a + b)


#Q2 write a program to input side of a square and find its area

#Ans-
S = float(input("Enter the side of the square: "))
X = S * S
print("The area of the square is: ", X)


#Q3 Write a program to input 2 floating numbers and print their average

#Ans-
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

z = (a + b)/2

print("the average of the numbers is: ", z)

#Q3 Write a program to input two int numbers and print true if 'a' is greater or equal to 'b'

#Ans-
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = a>=b
print(c)