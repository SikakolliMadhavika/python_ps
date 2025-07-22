# Very Important Basic Questions 
# Prime Number

def isPrime(num):
    if (num <=1):
        return "Not a Prime"
    for i in range(2, int((num**0.5))+1):
        if (num%i) == 0:
            return "Not a Prime"
    return "Prime"
print(isPrime(10))


# Palindrome for number
def isPalindrome(num):
    temp = num
    res=0
    while(temp):
        res = res*10 + (temp%10)
        temp//=10
    if(num == res):
        return "Palindrome"
    return "Not a Palindrome"
print(isPalindrome(1234321))
        

# Palindrome for string
def isPalindromeStr(str1):
    temp = str1
    clean=""
    res=""
    for i in temp:
        if(i.isalpha()):
            clean += i.lower()
            res = i.lower() + res
    if(clean==res):
        return "Palindrome"
    return "Not a Palindrome"
print(isPalindromeStr("mam"))


# Armstrong number 
def isArmstrong(num):
    if num < 0:
        return "Not an Armstrong"
    temp = num
    res = 0
    while(temp):
        res = res + (temp%10)**len(str(num))
        temp//=10
    return "Armstrong" if(num == res) else "Not an Armstrong"
print(isArmstrong(153))


# Factorial 
def factorial(num):
    if(num<0):
        return "Invalid"
    elif(num == 0 or num==1):
        return 1
    res = 1
    for i in range(2, num+1):
        res *= i
    return res
print(factorial(5))


# recursion version
def factorialRecursion(num):
    if(num<0):
        return "Invalid"
    elif(num==0 or num==1):
        return 1
    return num * factorialRecursion(num-1)
print(factorialRecursion(5))


# Swap two numbers 
def swapTwoNum(a,b):
    a,b = b,a
    return a,b
print(swapTwoNum(10,20))


# Swap two numbers using math
def swapTwoNum(a,b):
    a = a+b
    b=a-b
    a=a-b
    return a,b
print(swapTwoNum(10,20))


# Swap two numbers using temp
def swapTwoNum(a,b):
    temp = a
    a=b
    b=temp
    return a,b
print(swapTwoNum(10,20))


# Fibonacci 