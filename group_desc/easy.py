#Question - 1
# Create a function that takes two numbers as arguments and returns their sum.

def sumOfTwo(num1, num2):
    return num1+num2
print(sumOfTwo(10,11))


#Question - 2
# Write a function that takes an integer minutes and converts it to seconds.

def minToSec(min):
    if min<0:
        return "Invalid Input"
    return min*60
print(minToSec(2))


#Question - 3
# Create a function that takes a number as an argument, increments the number by +1 and returns the result.

def increment(number):
    return number+1
print(increment(11))


#Questiojn - 4
# Create a function that takes the age in years and returns the age in days.

def age(years):
    return years*365
print(age(2.6))


#Question - 5
# sbi Create a function that takes voltage and current and returns the calculated power.

def power(vol,curr):
    return vol*curr
print(power(20,40))


#Question - 6
# Write a function that returns the string "something" joined with a space " " and the given argument a.

def printing(name):
    return "Hello" + " " + name
print(printing('Madhu'))


#Question - 7
# Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.

def returning(numm1, numm2):
    if numm1 == 10 or numm2==10 or numm1+ numm2==10:
        return True
    return False 
print(returning(10,20))


# Question - 8
# Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

def stringcount(str1, str2):
    if len(str1 ) == len(str2):
        return True
    return False
print(stringcount("hello", "bye"))
print(stringcount("hii" , "bye"))

# Question - 9
# Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.

def greeting(name):
    return "Hii "+name
print(greeting("Madhu"))


# Question - 10
# Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).

def phone_format(list):
    format ="("
    for i in range(3):
        format += str(list[i])
    format+=")"
    for i in range(3,6):
        format += str(list[i])
    format +="-"
    for i in range(6,10):
        format += str(list[i])
    print(format)
phone_format([1,2,4,5,6,7,8,2,0,1])


# Question - 11
# Create a function that returns an array of strings sorted by length in ascending order.

def ascen_len(list):
    for i in range(0, len(list)-1):
        swap = True
        for j in range(0, len(list)-1):
            if len(list[j]) > len(list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
                swap = False
        if swap :
            return list
    return list
print(ascen_len(["a", "ccc", "dddd", "bb"]))


# Question - 12
# Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.

def largest_array(array):
    largest = []
    for list in array:
        max = list[0]
        for value in list:
            if max < value:
                max = value
        largest.append(max)
    print(largest)
largest_array([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]])


# Question - 13
# Create a function that takes an array of numbers and returns the second largest number.

def second_large(list):
    for i in range(0, len(list)-1):
        swap = False
        for j in range (0,len(list)-1):
            if list[j]<list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swap = True
        if not swap:
            return list[1]
    return list[1]
print(second_large([1,2,3,4,5,6,7]))


# Question - 14
# Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).

def remove_dup(list):
    new_list = []
    for i in list:
        if i  not in new_list:
            new_list.append(i)
    return new_list
print(remove_dup([1,2,1,2,1]))


# Question - 15
# Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array.

def unique_value(list1):
    unique = list(set(list1))
    for i in range(len(unique)):
        count = 0
        for j in range(len(list1)):
            if unique[i] == list1[j]:
                count +=1
        if count == 1:
            print(unique[i])
unique_value([2, 2, 2, 3, 4, 4, 4,5])



# Question - 16
# Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.

def charCount(char, string):
    if len(char) != 1:
        return "Invalid input"
    count = 0
    for i in string:
        if (i.lower() ==char):
            count+=1
    return count
print(charCount('a',"MadhavikaA"))
        

# Question - 17
# Create a function that takes a string and returns the number (count) of vowels contained within it.

def vowel_count(str):
    count = 0
    for i in str.lower():
        if i in ['a','e','i','o','u']:
            count+=1
    print(count)
vowel_count('MadhAvIka')


# Question 18
# Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.

def lower_upper(str):
    reverse = []
    for i in str:
        if(i.isupper()):
            reverse.append(i.lower())
        if(i.islower()):
            reverse.append(i.upper())
    print("".join(reverse))
lower_upper('MadhAvIKa')        

# without using is upper

def lower_upper(str):
    reverse = []
    for i in str:
        if(ord(i)>=65 and ord(i)<=90):
            reverse.append(i.lower())
        if((ord(i)>=97 and ord(i)<=122)):
            reverse.append(i.upper())
    print("".join(reverse))
lower_upper('MadhAvIKa') 


# Question - 19
# Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.

def multiply(num):
    print(num*2)
for i in range(1,6):
    multiply(i)


# Question - 20
# Create Function that will take one parameter and return type of the data.

def data_type(data):
    return type(data)
print(data_type("Hii"))
print(data_type(100.134))


# Question - 21
# Program to find greatest of three numbers(using ternary operator).

from statistics import _Number
def largest_of_three(num1, num2, num3):
        return num1 if (num1>num2 and num1>num3) else num2 if (num2>num1 and num2>num3) else num3 
print(largest_of_three(10,10,30))


# Question - 22
# C Program to find factorial of number.

def fact(number):
    fact = 1
    if number>=0:
        for i in range(2,number+1):
            fact*=i
        return fact
    return "Invalid input"
print(fact(5))


# Question - 23
# Program to arrange numbers in ascending order

def ascen_sorting(list):
    for i in range (0,len(list)-1):
        swap = False
        for j in range(0,len(list)-1):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swap = True
        if not swap :
            return list
    return list
print(ascen_sorting([1,2,3,4]))


# Question 24
# Print Patter using loop.

def pattern_print(rows, columns):
    for r in range(rows):
        for col in range(r+1):
            print(col+1, end = " ")
        print("")
pattern_print(5,5)


# Question - 25
# C Program to Calculate the Power of a Number(using loop only).

def power(number, power):
    res = 1
    for i in range(power):
        res*= number
    print(res)
power(2,4)


# Question - 26
# Program to Check Whether a Number is Prime or Not

def check_prime(number):
    if number<2:
        return str(number)+" is not a prime"
    for i in range(2, (number//2) +1):
        if number%i == 0:
            return str(number)+" is not a prime"
    return str(number)+" is a prime"
print(check_prime(2))


# Question - 27
# Program to find LCM of two numbers using while loop

def lcm_of_two(num1, num2):
    if num1 > num2:
        lcm = num1
    else :
        lcm = num2
    while True:
        if (lcm%num1 == 0) and (lcm%num2 ==0):
            return lcm
        lcm+=1
print(lcm_of_two(12,22))


# Question - 28
# Program to Display Characters from A to Z Using Loop with count.

def display_char():
    count = 1
    for i in range( 65,91):
        print(chr(i)+str(count))
        count+=1
display_char()

# Question - 29
# Program to find a missing number

def missing_number(len, list):
    for i in range(1,len+1):
        if i not in list:
            return i
print(missing_number(4,[2,3,4]))
            

# Question - 30
#  Program to count vowels and consonants in a given String.

def vowel_consonants(str):
    vow_count = 0
    cons_count = 0
    for i in str.lower():
        if i in ['a', 'e', 'i', 'o','u']:
            vow_count += 1
        elif i.isalpha():
            cons_count += 1
    print( vow_count,"Vowels",cons_count,"Consonants")
vowel_consonants("i am RAM")


# Question - 31
# program to insert  the elements of an array for specific index

def inserting(list, index, value):
    new_list = []
    for i in range(len(list)):
        if i == index:
            new_list.append(value)
        new_list.append(list[i])
    print(new_list)
inserting([1,2,3,4,5,7,8,9,10] ,5, 6)

        
# Question - 32
# Reverse a number using while Loop

def reverse(number):
    temp = number
    rev = 0
    while temp:
        rev = (rev*10) + temp%10
        temp//=10
    return rev
print(reverse(1234))

# Question - 33
# Count occurrence of number:

def occurance_of_number(list,number):
    count = 0
    for i in list:
        if i==number:
            count+=1
    print(count)
occurance_of_number([1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , 1)

