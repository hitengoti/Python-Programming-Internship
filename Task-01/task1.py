# Name: Goti Hiten Khodidasbhai
# Task 1 : 



# 1. Sum of Two Numbers - Take input & print their sum.
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
sum = a + b
print(f"Sum of {a} and {b} is: {sum}")



# 2. Odd or Even Checker - Check if a number is odd/even.
n = int(input("Enter Number(To Check Odd/Even): "))
print(f"Number {n} is even") if n%2==0 else print(f"Number {n} is Odd")



# 3. Factorial Calculation - Using a loop or recursion.

# using loop:
num = int(input("Enter Number(For Factorial): "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(f"Factorial of {num} is: {fact}")

# using recursion:
num = int(input("Enter Number(For Factorial): "))
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num * fact(num-1)
print(f"Factorial of {num} is: {fact(num)}")



# 4. Fibonacci Sequence - Generate first n numbers.
n = int(input("Enter Number(To Generate Fibonacci Sequence): "))
def fibo(n):
    n1,n2=0,1
    if n==1:
        print(f"Fibonacci Sequence: {n1}")
    elif n==2:
        print(f"Fibonacci Sequence: {n1} {n2}")
    else:
        print(f"Fibonacci Sequence: {n1} {n2}",end=" ")
        for i in range(n-2):
            n3 = n1+n2
            print(n3,end=" ")
            n1,n2 = n2,n3                   
fibo(n)



# 5. String Reverse - Reverse user-input string.
str=input("\n Enter String: ")
print(f"Reversed String is: {str[::-1]}")



# 6. Palindrome Check - Is the word same forward & backward?
word = input("Enter Word: ")
print(f"{word} is Palindrome.") if word==word[::-1] else print(f"{word} is NOT Palindrome.")



# 7. Leap Year Check - Check if a given year is leap year.
year=int(input("Enter Year(To Check Leap Year): "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")



# 8. Armstrong Number - Example: 153 -> 1^3 + 5^3 + 3^3 = 153.
y = input("Enter Number(To Check Armstrong Number): ")
n = len(y)
sum=0
for i in y:
    sum += int(i)**n
print(f"{y} is an Armstrong Number,") if int(y)==sum else print(f"{y} is not an Armstrong Number.")