# def first_last(first,last):
#     return first[0:3] + last[-3:]
# print(first_last("rahul", "sharma"))


# def first_last(first,last):
#     res = ""
#     for i in range(0,3):
#         res+=first[i]
#     for j in range(len(last)-3,len(last)):
#         res+=last[j]
#     return res
# print(first_last("rahul", "sharma"))


# def email_validator(mail):
#         if ('@' in mail) and ( ('.com' in mail) or ('.in' in mail) ):
#             return "valid email"
#         return "invalid mail"
# print(email_validator("madhu@.in"))
 

# def email_validator(mail):
#         flag1 = True
#         flag2 = True
#         for i in range(len(mail)):
#             if mail[i] == '@':
#                   one = 'com'
#                   two = 'in'
#                   for k in range(len(mail)):
#                         if mail[k] == '.':
#                                 for j in one:
#                                     if mail[k+1] == j:
#                                         k+=1
#                                     else:
#                                           flag1 = False
#                                           break
#                                 for y in two:
#                                         if mail[k+1] == y:
#                                             k+=1
#                                         else:
#                                               flag2 = False
#                                               break
#         if (flag1 or flag2):
#               return "Valid mail"
#         return "invalid mail"
# print(email_validator("madhu.in"))


# def count_words(line):
#     line = line.strip()
#     count = 0
#     for i in line:
#         if i==" ":
#             count += 1
#     return count+1
# print(count_words("      My name is Sikakolli Madhavika          "))

# def statement(item,cost):
#     # print(item + "costs")
#     return item + " costs " + str(cost)
# print(statement("Milk", 50))


# def palindrome(word):
#     low = 0
#     high = len(word)-1
#     while(low < high):
#         if (word[low] != word[high]):
#             return "Not a Plaindrome"
#         else:
#             low+=1
#             high-=1
#     return "Palindrome"
# print(palindrome("mam"))

# def initial_print(name):
#     for i in range(0,len(name)):
#         if name[i] == " ":
#             return name[0] + "." + name[i+1] + "." 
# print(initial_print("Sikakolli Madhavika"))


# def check(input, letter):
#     if letter in input:
#         return "Yes, the input contains the letter", letter
#     return "No, the input deosn't contains the letter", letter
# print(check("Madhavika",'s'))



# input = 'aaabbbcccaabb'
# output = ''
# count = 1
# for i in range(1,len(input)):
#     if input[i] == input[i-1]:
#         count +=1
#     else:
#         output += input[i-1] + str(count) + " "
#         count = 1
# print(output + input[-1] + str(count))



# # pattern
# n=5
# for i in range(n):
#     for j in range(n):
#         if (i>=j):
#             print("*",end=" ")
#     print()



# for i in range(10,21):
#     for j in range(1,11):
#         print(i,'*',j,'=',i*j)

# list1 = ['aaa', 'a', 'aaaa', 'aa']
# for x in range(len(list1)):
#     for y in range(len(list1)-1):
#         if len(list1[y]) > len(list1[y+1]):
#             list1[y], list1[y+1] = list1[y+1],list1[y]
# print(list1)


# k = 'python developer'
# cons = []
# for i in k:
#     if i not in 'aeiou ':
#         cons += [i]
# print(cons)
        


# l= [0,1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)):
#     if l[i]%2==0:
#         l[i] *=5
# print(l)


# str1 = 'aaabbccaabb'
# count = 1
# output = ""
# for i in range(1,len(str1)):
#     if str1[i] == str1[i-1]:
#         count += 1
#     else : 
#         output += str1[i-1] + str(count)
#         count = 1
# print(output + str1[-1] + str(count))



# l = [10, 1.34,'python', True, 200]
# for i in range(len(l)) :
#     if type(l[i]) == int:
#         l[i] *= 2
# print(l)
        

# for i in range(65,90):
#     print(chr(i))
# print(ord('A'))

# k = 'python developer'
# count =0
# for i in k:
#     if i in 'aeiou':
#         count+=1
# print(count)



# num = 153
# temp = num
# sum = 0
# while temp != 0:
#     digit = temp % 10
#     sum += (digit ** len(str(num)))
#     temp//=10
# if (num == sum):
#     print("Armstrong")
# else:
#     print("Not a armstrong")


# str1 = 'aaabbccaabb'
# count = 1
# for i in range(len(str1)):
#     if str1[i] 


# import random

# class Bank :
#     def __init__(self, name, accno):
#         self.H_Name = name
#         self.H_Acc = accno
#         self.Balance = 0
#         self.pin = random.randint(1000,9999)
#         print(f"Welcome {name}, your account has been created with a pin of {self.pin}")
        

#     def deposit(self,acc,money):
#         if (self.H_Acc == acc):
#             self.Balance += money
#         print(f"The current deposit is {money}, now the total balance is {self.Balance}")

#     def withdraw(self,acc,money):
#         if (self.H_Acc == acc):
#             self.Balance -= money
#         print(f"The current withdrawal is {money}, now the total balance is {self.Balance}")

#     def checkBal(self,acc):
#         if (acc == self.H_Acc):
#             print(f"The total balance is {self.Balance}")

# obj1 = Bank('Madhu', 8989)
# obj1.deposit(8989, 1000)
# obj1.withdraw(8989, 300)
# obj1.checkBal(8989)


# str1 = 'Madhu'
# new = ""
# for i in str1:
#     if ( ord(i)>64 and ord(i)<=90):
#         new += chr(ord(i) + 32)
#     else :
#         new += chr(ord(i) - 32)
# print(new)



         





# swapcase
# p = [1,2,3,4,5,6,8,10] input
# p =[1,(2,3), {4,5},(6,8,10)] output
# bank

# str1 = "Python Full Stack Developer"
# list1 = []
# count = 0
# for i in range(len(str1)):
#     if str1[i] == " ":
#         # list1.append(count)
#         list1 += [count]
#         count = 0
#     else:
#         count+=1
# print(list1 + [count])


# str1 = "Python Full Stack Developer"
# l = str1.split()
# count = 0
# for i in range(len(l)):
#     l[i] = len(l[i])
# print(l)


# int to string
# num1 = 1234
# m='0123456789'
# res=""
# while num1>0:
#     digit = num1%10
#     num1//=10
#     for x in range(len(m)):
#         if digit == x:
#             res = m[x] + res
# print(res, type(res))

# # str to int
# str1 = "5678"
# m = "0123456789"
# res = 0
# for i in range(len(str1)):
#     for j in range(len(m)):
#         if str1[i] == m[j]:
#             res = res*10 + j
# print(res)

# k = [1,2,3,4,5,6]
# avg = 0
# count = 0
# for i in k:
#     avg += i
#     count +=1
# print(avg/count)



# mail = 'madhusikakolli123@gmail.com'
# num =[]
# vow =[]
# con=[]
# spl =[]
# for i in mail:
#     if i in 'aeiouAEIOU':
#         vow += [i]
#     elif ( i not in 'aeiouAEIOU') and (ord(i)>64 and ord(i)<=90) or (ord(i)>96 and ord(i)<=122):
#         con += [i]
#     elif i in '0123456789':
#         num += [i]
#     else:
#         spl += [i]
# print("vowels :" , vow, "Consonants :", con, "nums : ",num, "spl : ", spl)


# k =[1,2,3]
# l = ['one', 'two', 'three']
# j={}
# for i in range(len(k)):
#     j[k[i]] = l[i]
# print(j)

# j = dict(zip(k,l))
# print(j)

# l = []
# n=3
# for i in range(n):
#     j = {}
#     j['pin'] = int(input("Enter pin :"))
#     j['Name'] = input("Enter Name")
#     j['Class'] = input("Enter Class")
#     l += [j]

# dict1 = {"hii" : 1, "hello" : 2}
# for i in dict1.items():
#     print(i)
    
# def calci(a,b):
#     def sum(a,b):
#         return a + b
#     def sub(a,b):
#         return a-b
#     def mul (a,b):
#         return a*b
#     def div(a,b):
#         return a/b
#     return sum(a,b), sub(a,b), mul(a,b), div(a,b)

# print(calci(20,10))

# k = 'I am going to USA'.split()
# for i in k:
#     if len(i) > 2 and len(i)<5 :
#         print(i)

# # area of triangle rectangle area of circle value of cylinder, cone
# def triangle (a,b):
#     print("Area of triangle is",a * b * 0.5)
# triangle(10,5)

# def rectangle (a,b):
#     print("Area of triangle is",a * b)
# rectangle(10,20)

# def circle(r):
#     print("Area of triangle is",3.14 * r* r)
# circle(10)

# def cone(s,r):
#     print("Area of cone is",(3.14*r * (s + r)))
# cone(12,11)

# def cylinder(h,r):
#     print("Area of cylinder is",(2 * 3.14 * r * (h + r)))
# cylinder(10,4)

    




# validate the registeration if user should enter username or mobile or email and pw and confirm pw should must

# def validation (user,pw,cpw):
#     if (user and pw and cpw):
#         if(pw == cpw):
#             print("User validation successful")
#         else:
#             print("Not validated")
#     else:
#         print("Fill feilds properly")

# validation('Madhu',123,12)



# for i in range(5):
#     for j in range(5):
#         if ( j==0 or j==4):
#             print("*", end = " ")
#         elif( i==j and i<=2) or (i+j == 4 and i<=2):
#             print("*", end =" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if(j==0 or i==0):
#             print("*",end=" ")
#     print()


# import keyword
# print(keyword.kwlist)

# dict1 = {'a' : 1, 'b':2, 'c':3}
# res = {a:b+10 for a,b in dict1.items() if b%2==0}
# print(res)


# list1 = [1,2,3,4,4,5]
# res = [a for a in list1 if a%2==0]
# print(res)


# list1  = [1,2,3,45,6,7,9,9]
# res = [a for a in list1 if a%2 != 0]
# print(res)


# list1 = ['app' , 'bat', 'cat', 'dog']
# res = [a for a in list1 if 'a' in a]
# print(res)

# list1 = [1,2,4,7,98,100,23]
# res = [x+100 for x in list1 if x%2==0 ]
# print(res)


# dict1 = {'a':12, 'b':23, 'c':34}
# res = {a:b//2 for a,b in dict1.items()}
# print(res)


# file handling :
# it means user can store some limited data permenantly
# methods : Open() Close() Name() Mode()
#  modes : 
# x : create empty file
# r : read data
# w : write data or create file
# a : append data
# R+ : read() write()
# W+ : write() read()
# A+ : append() read()



# def sum(list1):
#     res = 0
#     for i in list1:
#         res += i
#     return res
# print(sum([1,2,3,4,5])) 


# def perfect(num):
#     res = 1
#     for i in range(2,num//2+1):
#         if num%i ==0:
#             res += i
#     if(num == res):
#         return "Yes"
#     return "No"
# print(perfect(28))


# def strong(num):
#     temp = num
#     res =0
#     while temp>0:
#         digit = temp%10
#         temp//=10
#         fact =1
#         for i in range(2,digit+1):
#             fact*=i
#         res+=fact
#     if res == num:
#         return "Strong Number"
#     return "Not a strong number"
# print(strong(145))


# def validmail(mailid):
#     for i in mailid[:-10]:
#         if (not((i.isalpha()) or (i.isdigit()))):
#             # print(not ((i.isalpha()) or (i.isdigit()) ))
#             return "Invalid"
#     if (mailid[-10:] == '@gmail.com'):
#         return "Valid"
        
# print(validmail('madhu#@gmail.com'))
            

# def sumOfPrime(num):
#     while num>0:
#         digit = num%10
#         num//=10
#         flag = False
#         for i in range()
      