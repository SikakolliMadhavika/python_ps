# # Easy Level



# # Question - 1
# # to find +ve, -ve, zero

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

# def Even_Odd(number):
#     return "Even" if number%2 ==0 else "Odd"
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
#     if number <=0:
#         return "Invalid number"
#     days = ['Monday', 'Tuesday', 'Wednesday' , 'Thursday', 'Friday', 'Saturday', 'Sunday'];
#     return days[number-1]
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
# def printingvalueinlist(number):
#     if(number>=-(len(list1)) and number<len(list1)):
#         return (list1[number])
#     return "Invalid input"
# print(printingvalueinlist(5))
# print(printingvalueinlist(-5))



# def printingList(list1):
#     for i in list1:
#         print(i)
# printingList([3,4,5])


# def sumList(list1):
#     sum=0
#     for i in list1:
#         sum+=i
#     return sum
# print(sumList([3,4,5]))


# def sum_EvenIndex(list1):
#     sum=0
#     for i in range(0,len(list1),2):
#         sum+=list1[i]
#     return sum
# print(sum_EvenIndex([3,4,5,6,7]))


# def sum_EvenValues(list1):
#     sum=0
#     for i in list1:
#         if(i%2 ==0):
#             sum+=i
#     return sum
# print(sum_EvenValues([3,4,5,7,8]))


# def sum_EvenIndex_evenvalue(list1):
#     sum=0
#     for i in range(0,len(list1),2):
#         if(list1[i]%2 ==0):
#             sum+=list1[i]
#     return sum
# print(sum_EvenIndex_evenvalue([3,4,5,6,7,4,8]))


# def max_min_List(list1):
#     if(len(list1) == 0):
#         return "List is empty"
#     max=list1[0]
#     min=list1[0]
#     for i in list1:
#         if i>max:
#             max=i
#         if i<min:
#             min=i
#     return max,min        
# print(max_min_List([-3,-2,-8]))


# using slicing
# def reverse_list(list):
#     print(list[::-1])
# reverse_list([1,2,4,5,6,7])


# # using swaping
# def reverse_list_swap(list):
#     j=-1
#     for i in range(0,(len(list)//2)):
#         list[i],list[j] = list[j], list[i]
#         j-=1
#     print(list)
# reverse_list_swap([1,2,4,5,6,7])


# # using swapping and while loop
# def reverse_list_while(list):
#     low = 0
#     high = len(list)-1
#     while low < high:
#         list[low] , list[high] = list[high], list[low] 
#         low +=1
#         high -=1
#     print(list)
# reverse_list_while([1,2,3,4,45,56])


# # using extra memory and appending
# def reverse_list_new(list):
#     copy_list=[]
#     for i in range(-1,-len(list)-1,-1):
#         copy_list.append(list[i])
#     print(copy_list)
# reverse_list_new([1,2,4,5,6,7])


# # using extra memory and inserting
# def reverse_list_extra(list):
#     copy_list=[]
#     for i in range(0,len(list)):
#         copy_list.insert(0,list[i])
#     print(copy_list)
# reverse_list_extra([1,2,4,5,6,7])


# # using reverse inbuilt method
# def reverse_list_inbuilt(list1):
#     list1.reverse()
#     print(list1)
# reverse_list_inbuilt([1,2,3,3,4,565])


# # half list reverse 
# def half_reverse(list):
#     low = len(list)//2
#     high = len(list)-1
#     while low < high:
#         list[low] , list[high] = list[high], list[low]
#         low+=1
#         high-=1
#     print(list)
# half_reverse([1,2,3,5,8,9,65,44])


# # swappig types
# # first one

# a,b = 10,20
# a , b = b, a
# print(a,b)


# # using temp

# a,b = 10,20
# temp = a 
# a = b
# b = temp
# print(a,b)


# # using addition

# a,b = 10,20
# a = a+b
# b = a-b
# a = a-b
# print(a,b)


# # using xor

# a,b = 10,20
# a = a^b
# b = a^b
# a = a^b
# print(a,b)


# # return true or false while finding value in given list 
# def check_value(list, value):
#     return True if value in list else False

# print(check_value([1,647,767,768,2,4906],4906))

# # return index while finding value in given list 
# # linear search 
# def findvalueindex(list, value):
#     for i in range(len(list)):
#         if (list[i] == value):
#             return i
#     return -1

# print(findvalueindex([1,2,3,4,5,66],4))

# # finding duplicates and returning in list

# def find_dup(list1):
#     visited_list=[];
#     dup_set = set ();
#     for i in list1:
#         if i not in visited_list:
#             visited_list.append(i)
#         else:
#                 dup_set.add(i)
#     return list(dup_set), visited_list
# print(find_dup([1,2,3,4,2,2,6,5,6,66,1,1,1]))

# # findind duplicates in given number

# def dup_in_num(num):
#     temp = num;
#     uniq_list=[];
#     while temp:
#         digit = temp%10;
#         if digit in uniq_list:
#             return True
#         else : 
#             uniq_list.append(digit);
#         temp//=10;
#     return False
# print(dup_in_num(124))

# # find duplicates in return list of numbers

# def dup_in_num_list(list):
#     res_list = []
#     for i in list:
#         res_list.append(dup_in_num(i))
#     return res_list
# print(dup_in_num_list([1,234,222,3232,6789]))

# # binary search algorithm 

# def binary_search(list, search):
#     low = 0
#     high = len(list)-1
#     while (low <= high) :
#         mid = (low + high)//2
#         if (list[low] == search):
#             return low
#         elif (list[high] == search):
#             return high
#         elif (list[mid] == search):
#             return mid
#         elif list[mid] < search :
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# print(binary_search([1,6,10,44,78,92,100,110],72))

# # bubble sort 
# def bubble_sort(list1):
#     for i in range(len(list1)-1):
#         swap = True
#         for j in range(len(list1)-1-i):
#             if list1[j] > list1[j+1]:
#                 list1[j], list1[j+1] = list1[j+1] , list1[j]
#                 swap = False
#         if swap:
#             return list1
#     return list1
# print(bubble_sort([9,8,7,6,5]))


# # Date : 24-03-2025

# # rotate list values by k times

# def rotate_list(list1,k):
#     k = k % len(list1)
#     for i in range(k):
#         temp = list1[-1]
#         for j in range(len(list1)-1, 0, -1):
#             list1[j] = list1[j-1]
#         list1[0] = temp
#     return list1
# print(rotate_list([1,2,3,4,5],2))
















































# # find the given list is ascending sorted or not 

# def check_asec_sort(list):
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             return False
#     return True
# print(check_asec_sort([1,2,3,6,4,4]))

# # find the given list is decending sort or not 

# def check_desc_sort(list):
#         for j in range(len(list)-1):
#             if list[j] < list[j+1]:
#                 return False
#         return True
# print(check_desc_sort([5,4,5,3,2,1]))

# # find given list is asecnding or descending sorted

# def asec_desc_sort(list):
#     return check_asec_sort(list) or check_desc_sort(list) 
# print(asec_desc_sort([1,2,7,3,4,5,6]))

# # find second largest value in list using sorting
# def sorting(temp):
#     temp = list(set(temp))
#     for i in range(len(temp)-1):
#         for j in range(len(temp)-1):
#             if temp[j] > temp[j+1]:
#                 temp[j], temp[j+1] = temp[j+1], temp[j]
#     return temp[-2] if len(temp)>1 else "No second largest value"
# print(sorting([5,4,4,5,7,7,3,2,1]))
# print(sorting([1]))

# def second_largest(list1):
#     first_max = list1[0]
#     for i in list1:
#         if i > first_max:
#             first_max = i
#     sec_max = list1[0]
#     for i in list1:
#         if i > sec_max and i!= first_max:
#             sec_max = i
#     return sec_max
# print(second_largest([1,5,7,8,9,3,2,5,8,9,9]))
# second_largest([9,8,7,6,5,4,4])
    
# def merge_lists(list1, list2):
#     res_list = []
#     i,j = 0,0
#     while (i < len(list1) ) and (j < len(list2)) :
#         if(list1[i] < list2[j]):
#             res_list.append(list1[i])
#             i+=1
#         else :
#             res_list.append(list2[j])
#             j+=1
#     res_list.extend(list1[i:])
#     res_list.extend(list2[j:])
#     return res_list

# print(merge_lists([1,3,5,7,9,9,9],[2,4,6,10]))
    
# Recursion 
# def printing(num):
#     if num == 0:
#         return
#     printing(num-1)
#     print(num)
# printing(5)


# def fact(num):
#     if num == 1:
#         return 1
#     res = fact(num-1)
#     return num * res
# print(fact(5))


# def sum(num):
#     if (num == 0):
#         return 0
#     return sum(num - 1) + num
# print(sum(5))
    

# def reverse(str):
#     if len(str) <= 1:
#         return str
#     return str[-1] + reverse(str[0:-1])
# print(reverse("madhu"))

# def power(a,b ):
#     if b == 0:
#         return 1
#     return a * power(a, b-1)
# print(power(2,5))

# def count_list(list):
#     if len(list) == 0:
#         return 0
#     return 1 + count_list(list[0:-1])
# print(count_list([1,2,3,4,5]))

# def isPalindrome(str):
#     if len(str) <= 1:
#         return "Palindrome"
#     if (str[0] == str[-1]) and  isPalindrome(str[1:-1]):
#         return "Palindrome"
# print(isPalindrome("madam"))

# def fabi(num) :
#     if num<0:
#         return "Not valid"
#     if num <= 1:
#         return num
#     return fabi(num-1) + fabi(num-2)
# print(fabi(5))

# def max_value(list1):
#     if len(list1) == 0:
#         return "No values"
#     if len(list1) == 1:
#         return list1[0]
#     return list1[0] if list1[0] > max_value(list1[1:]) else max_value(list1[1:])
# print(max_value([1,7,9,3,10]))

# def listval_occu(list1):
#     dict1 = {}
#     for i in list1:
#         if i in dict1:
#             dict1[i] += 1
#         else:
#             dict1[i] = 1
#     return dict1
# print(listval_occu([1,1,1,2,2,78,91,3,4,5,1]))

# def word_list(list1):
#     dict1 = {}
#     for i in list1:
#         dict1[i] = len(i)
#     print(dict1)
# word_list(['hii', 'helloooo', 'world', 'byee'])


# def char_str(str):
#     dict1 = {}
#     for i in str.lower():
#         if i in dict1:
#             dict1[i] +=1
#         else:
#             dict1[i] = 1
#     print(dict1)
# char_str("appleA  ")

# def merge_lists(list1, list2):
#     dict1 = {}
#     for i in range(0, len(list1)):
#         dict1[list1[i]] = list2[i]
#     print(dict1)
# merge_lists([1,2,3,4], [5,6,7,8])

# def sock_pairs(list1):
#     dict1 = {}
#     for i in list1:
#         i = i.lower()
#         if i in dict1:
#             dict1[i]+=1
#         else:
#             dict1[i] = 1
#     pairs = 0
#     for x,y in dict1.items():
#         pairs += y//2
#     print(pairs)
#     if pairs >= 6:
#         print("I can sustain")
#     else:
#         print("Not sufficient")

# sock_pairs(['red', 'Black', 'blue', 'rEd', 'black'])

# def merge_dicts(dict1, dict2):
#     for x,y in dict2.items():
#         if x in dict1:
#             dict1[x] += y
#         else:
#             dict1[x] = y
#     return dict1
# print(merge_dicts({"hi" : 1, "hello" : 2, "bye" : 3}, {"world" : 5, "bye" : 2, "guys" : 7}))

# def swap_key_value(dict1):
#     res_dict = {}
#     for i,j in dict1.items():
#         if j in res_dict:
#             res_dict[j].append(i)
#         else:
#             res_dict[j] = [i]
#     return res_dict
# print(swap_key_value({"hii" : 10, "hello" : 20 , "hi" : 30, "bye" : 30}))

# def high_value_dict(dict1):
#     max = float('-inf')
#     max_key = "No key"
#     for i,j in dict1.items():
#         if j>max:
#             max = j
#             max_key = i
#     print(max_key)
# high_value_dict({"hii" : 10, "hello" : 20 , "hi" : 30, "bye" : 40})

from abc import ABC, abstractmethod


mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# # printing matrix  
# for i in mat1:
#     for j in i:
#         print(j)

# # printing matrix using indexes
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         print(mat1[row][col])

# # printing output in matrix form
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         print(mat1[row][col], end = " ")
#     print()

# # printing diagnol val in matrix
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if row == col:
#             print(mat1[row][col])

# # printing upper triangle values
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if row < col:
#             print(mat1[row][col])

# # printing lower triangle values
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if row > col:
#             print(mat1[row][col])

# # printing boundary values
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if (row == 0 or row == len(mat1)-1 or col == 0 or col == len(mat1[row])-1):
#             print(mat1[row][col], end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# # sum of boundary elements
# max = 0
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if (row == 0 or row == len(mat1)-1 or col == 0 or col == len(mat1[row])-1):
#             max += mat1[row][col]
# print(max)


# # printing another diaglonal
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if (row + col == len(mat1)-1):
#             print(mat1[row][col])

# # sum of both diagnal values
# sum = 0
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if (row == col) or (row + col == len(mat1)-1) :
#             sum += mat1[row][col]
# print(sum)

# # sum of two matix
# mat3 = [
#     [1,2],
#     [3,4]
# ]
# mat2 = [
#     [5,6],
#     [7,8]
# ]
# for row in range(len(mat2)):
#     for col in range(len(mat2[row])):
#             mat2[row][col] += mat1[row][col]
#             print(mat2[row][col], end=" ")
#     print()


# # transpose of a matrix
# for row in range(len(mat1)):
#     for col in range(len(mat1[row])):
#         if row < col:
#             mat1[row][col], mat1[col][row] = mat1[col][row], mat1[row][col]
#         print(mat1[row][col], end = " ")
#     print()

# # remove braces
# str1 = 'a+((b-c)+d)'
# resstr = ""
# for i in str1:
#     if i != '(' and i != ')':
#         resstr += (i)
# print(resstr)


# # string palindrome
# str1 = 'madhu'
# resstr = ""
# print(str1[::-1])

# for i in range(len(str1)-1,-1,-1):
#     resstr += str1[i]
# print(resstr)


# def strpal(str1):
#     low = 0
#     high = len(str1)-1
#     while low < high :
#         if str1[low] == str1[high]:
#             low +=1
#             high -=1
#         else :
#             return "Not a Palindrome"
#     return "Palindrome"
# print(strpal('madam'))

# # finding no.og vowels consonants spaces
# def vow_con_space(str):
#     vow_count = 0
#     con_count = 0
#     space_count = 0
#     for i in str:
#         if i in ['a', 'e', 'i', 'o', 'u']:
#             vow_count +=1
#         elif i == ' ':
#             space_count +=  1
#         elif i.isalpha() :
#             con_count +=1
#     print(vow_count, con_count, space_count)
# vow_con_space('hii this is madhu')

# def non_rep_vow(str1):
#     resstr = ''
#     for i in str1:
#         if i.count == 1:
#             resstr += i
#     print(resstr)
# non_rep_vow('aaaeiouuu')

# largest word in given string
# def large_word(str):
#     max = 0
#     for i in str.split():
#         if len(i) > max:
#             max = len(i)
#     for i in str.split():
#         if len(i) == max:
#             print(i)
# large_word('Hii guys this is Madhavika sikakolli')

# # most repeated chars
# def most_rep_word(str):
#     dict1 = {}
#     for i in str.split():
#         count = 0
#         for j in i:
#             if i.count(j) > 1:
#                 count += 1
#         dict1[i] = count
#     max = 0
#     word = ''
#     for i,j in dict1.items():
#         if max < j:
#             max = j
#             word = i
#     print(word)
# most_rep_word('google microsoft')    

# # patterns
# def square(row, col):
#     for r in range(row):
#         for c in range(col):
#             print('*', end = " ")
#         print()
# square(4,4)

# # longest substring palindrome
# def long_pal_substr(str1):
#     sub_str_list = []
#     for i in range(len(str1)):
#         for j in range(i+1, len(str1)+1):
#             sub_str_list.append(str1[i:j])

#     pal_substr_list = []
#     max = 0
#     for i in sub_str_list:
#         if i == i[::-1]:
#             pal_substr_list.append(i)
#             if len(i) > max:
#                 max = len(i)
#     for i in sub_str_list:
#         if len(i) == max:
#             print(i)

# long_pal_substr('abc')


# #  longest substring palindrome
# def long_pal_substr(str1):
#     res_str = ""
#     for i in range(len(str1)):
#         for j in range(i+1, len(str1)+1):
#             sub_str = str1[i:j]
#             if sub_str == sub_str[::-1]:
#                 if len(sub_str) > len(res_str):
#                     res_str = sub_str
#     print(sub_str)
# long_pal_substr('abc')


# str1 = "takeyouforward"
# str2 = "forward"
# for i in range(len(str1)):
#     if  str1[i:i+7] == str2 :
#         print(i)


# for i in range(6):
#     for j in range(6):
#         if i >= j:
#             print('*', end = " ")
#     print()


# for i in range(6):
#     for j in range(6):
#         if i <= j:
#             print('*', end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# for i in range(6):
#     for j in range(6):
#         if i == 0 or j==0 or i==5 or j ==5:
#             print('*', end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# for i in range(6):
#     for j in range(6):
#         if i == 0 or j ==0 or i == 5 or j ==5 or i==j or i+j == 5:
#             print('*', end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# for i in range(6):
#     for j in range(6):
#         if i == 0  or i == 5 or i==j or i+j == 5:
#             print('*', end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# for i in range(6):
#     for j in range(6):
#         if  j ==0  or j ==5 or i==j or i+j == 5:
#             print('*', end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# for i in range(6):
#     for j in range(6):
#         if j==0 or i==j or i==5:
#             print('*', end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# num = 1
# for i in range(6):
#     for j in range(6):
#         print(num , end = " ")
#         num+=1
#     print()


# num = 65
# for i in range(6):
#     for j in range(6):
#         if i >= j:
#             print(chr(num) , end = " ")
#             num+=1
#     print()


# class Calculator :
#     max_count = 100 #class or static variable
#     def __init__(self,date):
#         print("Constructor is called")
#         self.manu_date = date # instance variable

#     # instance method
#     def details_meth(self):
#         print(self.manu_date)

#     # class method
#     @classmethod
#     def detail_cl(cls, max):
#         cls.max_count = max
#         print(cls.max_count)

#     @staticmethod
#     def description():
#         print("Hello Guysss")

#     def add():
#         print('add')
#     def sub():
#         print('sub')

# obj1 = Calculator('18Feb2022')
# # print(obj1.manu_date)
# # print(vars(obj1))
# # print(Calculator.max_count)
# # obj1.details_meth()
# # Calculator.detail_cl('12')
# # print(obj1.max_count)
# # Calculator.description()
# # obj1.description()



# class Cal():
#     def __init__(self, name1, date1):
#         print("Calc constructor")
#         self.name = name1
#         self.date = date1

#     def add(self,a,b):
#         print(a+b)

#     def sub(self,a,b):
#         print(a-b)

# class AdvCal(Cal):

#     def __init__(self, name1, date1,id):
#         super().__init__(name1, date1)
#         self.num = id
#         print("AdvCal constructor")

#     def add(self, a,b):
#         print("Now added", a+b)

#     def mul(self,a,b):
#         print(a*b)

    
# class ScienCal(AdvCal):
#     pass

# adv1 = AdvCal('Casio', '24Sep', '24')
# adv1.add(13,24)


# class Lion():

#     def roar():
#         print("Lion is Roaring")

# class Tiger():

#     def hunt():
#         print("Tiger is hunting")

# class Liger(Lion, Tiger):

#     pass

# liger = Liger()
# print(Liger.mro())


# Encapsulation - binding data with methods, it enhances security

# class HumanBeing():

#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

#     def get_Name(self):
#         return self.__name
    
#     def set_Name(self, new_name):
#         self.__name = new_name

# hm1 = HumanBeing('Madhu', 21)

# print(hm1.get_Name())
# hm1.set_Name('Madhavika')
# print(hm1.get_Name())
# # print(hm1.name)


# class Lion():

#     def __init__(self):
#         print("Lion is Roaring")

# class Tiger():

#     def __init__(self):
#         print("Tiger is hunting")

# class Liger(Lion, Tiger):

#     def __init__(self):

#         super().__init__()
#         print("Liger is here")

# liger = Liger()

# # abstraction - hides the implementation details of methods
# class ATM(ABC):

#     @abstractmethod
#     def withdrawal(self):
#         pass

#     @abstractmethod
#     def check_bal(self):
#         pass

#     @abstractmethod
#     def deposit(self):
#         pass

#     def machine_details(self):
#         pass

# class SBI_ATM(ATM):

#     def withdrawal(self):
#         print("SBI withdrawal")

#     def check_bal(self):
#         print("SBI check balance")

#     def deposit(self):
#         print("SBI deposit")

# sbi = SBI_ATM()

# class HDFC_ATM(ATM):

#     def withdrawal(self):
#         print("HDFC withdrawal")

#     def check_bal(self):
#         print("HDFC check balance")

#     def deposit(self):
#         print("HDFC deposit")

# hdfc = HDFC_ATM()

n = 5
# for i in range(n):
#     for k in range(n-i-1):
#         print(" ",end="")
#     for j in range(n):
#         if i >= j:
#             print("*", end=" ")
#     print()


# for i in range(n):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(n):
#         if i <= j:
#             print("*", end=" ")
#     print()


# for i in range(n):
#     for k in range(n-i):
#         print(" ",end="")
#     for j in range(n):
#         if i > j:
#             print("*", end=" ")
#     print()
# for i in range(n):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(n):
#         if i <= j:
#             print("*", end=" ")
#     print()



# for i in range(n):
#     count = 1
#     for s in range(n-1-i):
#         print(" ",end="")
#     for k in range(n):
#         if i>=k:
#             print(count, end = " ")
#             count+=1
#     print()


# a=0
# b=1
# n=4
# for i in range(n):
#     for s in range(n-1-i):
#         print(" ",end="")
#     for k in range(n):
#         if i>=k:
#             print(a, end = "  ")
#             a,b = b, a+b
#     print()

# for i in range(n):
#     num = 0
#     val = 1
#     for s in range(n-1-i):
#         print(" ",end="")
#     for k in range(n):
#         if i>=k and i%2==0:
#             print(num, end = " ")
#             num = 0 if num == 1 else 1
#         elif i>=k and i%2!=0:
#             print(val, end = " ")
#             val = 0 if val == 1 else 1
#     print()


# for i in range(n):
#     for s in range(n-i-1):
#         print(" ", end="")
#     for j in range(n):
#         if i >= j:
#             print((i + j) % 2, end=" ")
#     print()


# n=6
# for i in range(n):
#     start = i + 1
#     track = True
#     for s in range(n-i-1):
#         print(" ",end=" ")
#     for j in range((i*2)+1):
#         print(start,end=" ")
#         if start == 1:
#             track = False
#         start = start-1 if track else start + 1
#     print()

import copy
arr = [55,64,3,2,101]
temp = sorted(arr)
# temp = []
# for i in arr:
#     temp.append(i)
# temp = copy.deepcopy(arr)
res = []

# for i in range(len(temp)):
#     for j in range(len(temp)-1):
#         if temp[j] > temp[j+1]:
#             temp[j], temp[j+1] = temp[j+1],temp[j]
# print(temp)

# for i in arr:
#     res.append(temp.index(i)+1)
# print(res)

# class Car :
#     def __init__(self, color):
#         self.color = color
#     def describe(self):
#         print(f"Car color is {self.color}")
# myCar = Car("Blue")
# myCar.describe()

# class Animal:
#     pass