# # Easy Level


# # Question - 1
# # to find +ve, -ve, zero
# num = float(input())
# if num == 0:
#     print("Zero")
# elif num>0:
#     print("Positive")
# else:
#     print("Negative")


# def posNeg(number):
#     if number == 0:
#         return "Zero"
#     elif number>0:
#         return "Positive"
#     return "Negative"
# print(posNeg(0))
# print(posNeg(2))


# # Question - 2
# # to find even or odd
# num = float(input())
# if num%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# num = float(input())
# res = "Even" if num%2 == 0 else "Odd"
# print(res)


# def Even_Odd(number):
#     if number%2 == 0:
#         return "Even"
#     return "Odd"
# print(Even_Odd(24))
# print(Even_Odd(3))


# # Question - 3
# # to find eligible for vote or not
# def Vote(age):
#     if age>=18:
#         return "Eligible"
#     return "Ineligible"
# print(Vote(2))
# print(Vote(25))


# age = int(input())
# res = "Eligible" if age>=18 else "Ineligible"
# print(res)


# # Question - 4
# # to find greatest of two
# def Greatest(num1, num2):
#     if num1>num2:
#         return num1
#     return num2
# print(Greatest(10,11))
# print(Greatest(-10,0))


# # Question - 5
# # to find pass or fail or student
# def student_grade(marks):
#     if marks>40:
#         return "Pass"
#     return "Fail"
# print(student_grade(42))
# print(student_grade(32))


# # Question - 6
# # to find day of the week
# def week_day(number):
#     if number ==1:
#         return "Monday"
#     elif number ==2:
#         return "Tuesday"
#     elif number ==3:
#         return "Wednesday"
#     elif number ==4:
#         return "Thursday"
#     elif number ==5:
#         return "Friday"
#     elif number ==6:
#         return "Saturday"
#     elif number ==7:
#         return "Sunday"
#     return "Invalid"
# print(week_day(7))
# print(week_day(-2))


# # Question - 7
# # to make calculate 
# def calci(operator, num1,num2):
#     operation = operator.lower()
#     if operation == "add":
#         return num1 + num2
#     elif operation == "sub":
#         return num1 - num2
#     elif operation == "mul":
#         return num1 * num2
#     elif operation == "div":
#         if num2 == 0:
#             return "Division by 0 Error"
#         return num1 / num2
#     return "Invalid"
# print(calci('Add', 10, 20))
# print(calci('muld', 30,40))


# # Question - 8
# # to find month
# def month(number):
#     if number ==1:
#         return "January"
#     elif number ==2:
#         return "Febraury"
#     elif number ==3:
#         return "March"
#     elif number ==4:
#         return "April"
#     elif number ==5:
#         return "May"
#     elif number ==6:
#         return "June"
#     elif number ==7:
#         return "July"
#     elif number ==8:
#         return "August"
#     elif number ==9:
#         return "September"
#     elif number ==10:
#         return "October"
#     elif number ==11:
#         return "November"
#     elif number ==12:
#         return "December"
#     return "Invalid"
# print(month(7))
# print(month(9))


# def months(num):
#     if num<=12 and num>0:
#         month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         return month[num-1]
#     return 'Invalid input'
# print(months(3))


# Medium Level
# # Question - 1 - 4
# def vowel_cons(char):
#     char = char.lower()
#     if len(char) != 1:
#         return "Invalid character input"
#     elif char.isalpha():
#         if char in ['a', 'e', 'i', 'o', 'u']:
#             return "Vowel"
#         return "Consonant"
#     return "Neither Vowel nor Consonant"
# print(vowel_cons('A'))
# print(vowel_cons('Absy'))
# print(vowel_cons('12'))
# print(vowel_cons('$'))



# # Question - 2a - 1
# def print100():
#     for i in range(1,101):
#         print(i)
# print100()


# #Question - 2a - 2
# def sumOfnum(num):
#     return (num*(num+1))//2
# print(sumOfnum(3))
# print(sumOfnum(10))


# # Question - 2a - 3
# def printeven():
#     num = 2
#     while num<=50:
#         print(num)
#         num += 2
# printeven()


# # Question - 2a - 4
# def table(num):
#     for j in range(1,num+1):
#         for i in range(1,21):
#             print(j,"*",i,"=",j*i)
# table(10)
# table(2)


# def table(num):
#         for i in range(1,21):
#             print(num,"*",i,"=",num*i)
# # table(10)
# table(2)



# # Question - 2a - 5
# def reverse_and_sum(num):
#     sum = 0
#     rem = 0
#     rev = 0
#     while num>0:
#         rem = num % 10
#         sum += rem
#         rev = (rev*10) + rem
#         num = num//10
#     return "Reverse number is",rev,"Sum of digits is",sum
# print(reverse_and_sum(123))
# print(reverse_and_sum(12321))

# # using string coversion
# def reverse(number):
#     print( str(number)[::-1])
# reverse(12345)
# reverse(134576)

# def reverse(number):
#     con = str(number)
#     sum = 0
#     for i in range(len(con)):
#         sum+=int(con[i])
#     print("Sum is ", sum)
#     print("Reverse number is", con[::-1])
# reverse(12345)
# reverse(134576)

# # Question - 2a - 6
# def count_of_digits(number):
#     count = 0
#     rem1 = 0
#     while number>0 :
#         rem1 = number % 10
#         count+=1
#         number = number//10
#     return count
# print(count_of_digits(123456))
# print(count_of_digits(1029374))
         

# # Question - 2a - 7
# def take_input():
#     num = int(input("Enter a number"))
#     while(num>=0):
#         num = int(input("Enter a number"))
# take_input()


# # Question - 2b - 1
# def fabinocci(num):
#     fab_list = [0,1]
#     for i in range(num):
#         if i>1:
#             fab_list.append(fab_list[i-1] + fab_list[i-2])
#         # print(fab_list[i])
#     return fab_list
# print(fabinocci(5))
# print(fabinocci(15))


# #  without using function
# num = int(input("Enter number : "))
# num1 = 0
# num2 = 1
# if num>= 0:
#     print(num1)
# if num >= 1:
#     print(num2)
# for i in range(0,num-2):
#     temp = num1 + num2
#     print(temp)
#     num1 = num2
#     num2 = temp

# #  without using function
# num = int(input("Enter number : "))
# num1 = 0
# num2 = 1
# sum=0
# for i in range(0,num):
#     print(num1)
#     # sum+=num1
#     num1, num2 = num2, num1 + num2
#     # temp = num1 + num2
#     # num1 = num2
#     # num2 = temp
# # print(sum)

# # Question - 2b - 2
# def prime(num):
#     if num <= 1:
#         return "Neither Prime nor Composite"
#     for i in range(2,(num//2)+1):
#         if num%i == 0:
#             return "Not a Prime Number"
#     return "Prime Number"
# print(prime(0))
# print(prime(24))
# print(prime(5))


# #  without function
# num = int(input("Enter any number : "))
# if num<=1:
#     print("Neither Prime nor Composite")
# else :
#     spy = True
#     for i in range(2, num):
#         if (num%i == 0):
#             spy = False
#             break
#     if spy:
#         print("Prime Number")
#     else :
#         print("Not a Prime Number")

# # four approaches of range
# 1 - 1, num+1
# 2 - 2, num
# 3 - 2, num//2 + 1
# 4 - 2, (num**0.5)+1

# # Question - 2b - 3
# def factorial(number):
#     if number>=0:
#         fact = 1
#         start = 1
#         while start<number:
#             start +=1
#             fact*=start
#         return fact
#     return "Invalid input"
# print(factorial(3))
# print(factorial(0))
# print(factorial(-3))


# # Question - 2b - 4
# def printing():
#     for i in range(1,101):
#         if i%3 ==0 and i%5==0:
#             print(i)
# printing()


# # Question - 2b - 5
# def userfun(choose, num):
#     if choose == 1:
#         return num**2
#     elif choose == 2:
#         return num**3
#     elif choose == 3:
#         return None
#     else :
#         return "Invalid"
# print(userfun(1,3))
# print(userfun(2,3))
# print(userfun(3,3)) 
# print(userfun(10,3))


# # Question - 2b - 6
# def login():
#     password = 1234
#     for i in range(3):
#         user_pass = int(input("Enter your password :"))
#         if user_pass == password:
#             return "Login Succesful"
#         elif i!= 2 :
#             print("Incorrect Password Only",2-i , "attempts left")
#     return "Out of 3 Attempts"
# print(login())



# #  sum of odd in given number
# def sumOfOdd(num):
#     sum =0
#     while(num):
#         if((num%10)%2 != 0):
#             sum+= num%10
#         num//=10
#     return sum
# print(sumOfOdd(2345))



# def primeNumber(number):
#     if number <= 1:
#         return False
#     for i in range(2, number//2+1):
#         if (number%i == 0):
#             return False
#     return True

# # sum of non primes
# def sumOfNonPrimes(number):
#     sum=0
#     while(number):
#         digit = number %10
#         if (primeNumber(digit) == False ):
#             sum+=digit
#         number//=10
#     return sum
# print(sumOfNonPrimes(2345546))


# # armstrong number

# n = int(input("Enter a number : "))
# temp = n
# sum = 0
# while(temp):
#     sum+= (temp%10)**len(str(n))
#     temp//=10
# if(sum == n):
#     print("Armstrong")
# else:
#     print("Not a Armstrong")


# # armstrong number
# def armstrong(number):
#     temp = number
#     temp2 = number
#     sum=0
#     while(temp):
#         sum+= (temp%10)** len(str(temp2))
#         temp//=10
#     if(sum == temp2):
#         print("Armstrong")
#     else:
#         print("Not an Armstrong")
# armstrong(153)
# armstrong(1234)


# #  armstrong number in range
# def armstrongg(number):
#     temp = number
#     temp2 = number
#     sum=0
#     while(temp):
#         sum+= (temp%10)** len(str(temp2))
#         temp//=10
#     if(sum == temp2):
#         return True
#     return False

# def armstronginRange(num1, num2):
#     for i in range(num1, num2+1):
#         if(armstrongg(i)):
#             print(i)
# armstronginRange(1,100)



# # nearest prime
# def nearestPrime(number):
#     temp_left = number
#     temp_right = number
    


# # Palindrome     

# def check_palindrome(number):
#     temp = number
#     rev=0
#     while temp!=0:
#         rev = rev*10 + (temp%10)
#         temp//=10
#     if(rev == number):
#         return True

# def palindrome(num):
#     if(check_palindrome(num)):
#         return "Palindrome"
#     return 'Not a Palindrome'

# print(palindrome(1234))
# print(palindrome(32323))


# #iterating in list
# list1 = [1,23, 2.43, True, False]

# for i in list1:
#     print(i)

# for i in range(len(list1)):
#     print(list1[i])

# i=0
# while i<len(list1):
#     print(list1[i])
#     i+=1

# k=int(input("Enter number2 :"))

# if k<1 and k>len(list1):
#     print("Enter valid number")
# else:
#     print(list1[k-1])


# def alternatePrint(str):
#     new = []
#     for i in range(len(str)):
#         if i%2 == 0:
#             new.append(str[i].upper())
#         else:
#             new.append(str[i].lower())
#     print("".join(new))
# alternatePrint('madhavika')


# max in list
def max