#declaration of different datatypes
num1=10 #int
num1=2.0 #float
str="keerthi" #string
bool=True #boolean
list1=["kerala","kochi","tamilnadu",] #list
tup1=(1,2) #tuple
dict1={"salaar":"1","baahubali":"2","sahoo":"3" } #dictionary
set1={"pb","ssmb","aa"} #set
num=None #none

#conditional statements-if, else,elif
#if andelse statemnts
num1=0
if num1>=0:
    print("positive")
else:
    print("negative")

#elif
num2=0
if num2==0:
    print("positive")
elif num2==-1:
    print("zero")
elif num2==0:
    print("-1")
elif num2==2:
    print("-2")
else:
    print("negative")


#loops-for, while,
for i in range(0,21):
    print(i)
    print("hello")
    print("keerthi")

    #even and odd using loops
for j in range(0,20):
    if j % 2 == 0:
         print( "even number")
    else:
        print( "odd number")


#even num step
for i in range(0,21,2):
    print(i)

#odd
for i in range(1,21,2):
    print(i)

#even and odd using while loop
num = 6
while num < 20:
    if num % 2 == 0:
        print(num,"Even")
    else:
        print(num,"Odd")
    num += 1

#jump statements-break continue
#break
for i in range(0,21):
    if i==6:
        print(i)
        break
    print(i)

#continue
for i in range(0,21,2):
    if i==5:
        continue
    print(i)

#functions
def sumOfTwoNumbers(a,b):
    print("sum of two numbers",a+b)
sumOfTwoNumbers(5,3)

def even_or_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(22))

#inbuilt functions->string,list
text="keerthi"
print(text[0:5])

str1="naru"
str2="keerthi"
print(str1+" "+str2)
print(str1+str2)
print(str1 *3)
print(str1.strip())
print(str1.lower())
print(str1.upper())
print(str2.replace("keerthi","sukeerthi"))
print(str1.find("ar"))
print(str1.split(",,"))

str3=["rinku","20"]
print(",,".join(str3))
list=[1,2,3,4]
list.append(5)
print(list)


numbers=[1,2]
print(numbers[1])
print(numbers[0:2])
print(len(numbers))
print(2 in numbers)
l1=[1,2,3,4]
l2=[4,3,2,4]
print(l1+l2)
l1.extend([2,3])
print(l1)
l1.insert(4,8)
print(l1)
l1.pop(3)
print(l1)
print(l1.index(3))
l1.reverse()
print(l1)
l1.sort()
print(l1)
s1={1,2}
s5={2,3}
s6={3,4}
s7={7,8,4}
print(s1.union(s5,s6,s7))
l={1,2,3,4}
l.clear()
print(l)
set1={1,2,3,4,5,2}
set2={2,3,6,8,3,4,9}
print(set1 | set2)
set1={1,2,3,4}
set2={1,2,3,4,5,6,74,56}
print(set2.union(set1))
