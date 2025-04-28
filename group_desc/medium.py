# # Question - 2
# # Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length.

# def multiples_array(num, length):
#     mul_arr=[]
#     for i in range(1,length+1):
#         mul_arr.append(num*i)
#     return mul_arr
# print(multiples_array(17,6))

# # Question - 3
# # Create the function that takes an array with objects and returns the sum of people's budgets.

# def getBudgets(list1):
#     sum = 0
#     for i in list1:
#         sum += i["budget"]
#     print (sum)
# getBudgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }])

# # Question - 4
# # Create a function that takes an array of objects like { name: "John", notes: [3, 5, 4]} and returns an array of objects like { name: "John", avgNote: 4 }. If a student has no notes (an empty array) then let's assume avgNote: 0.

# def avd_note(list1):
#     for x,y in list1[0].items():
#         avg = 0
#         if x == "notes":
#             for z in y:
#                 avg += z
#             avg = avg//len(y)
#     del list1[0]["notes"]
#     list1[0]["avgNote"] = avg
#     print(list1[0])
# avd_note([{ "name": "John", "notes": [3, 5, 4]}])

# # Question - 7
# # Write a function that accepts an array of strings. Return the longest string(can not use predefined function).

# def long_str(list1):
#     max = list1[0]
#     for i in list1:
#         if len(i) > len(max):
#             max = i
#     return max
# print(long_str(['nik', 'mikhil', 'Cow','Elephant']))

# # Question 9
# # Write Program to remove duplicate elements in an array and sort it in descending order(can not use predefined function).

# def desc_sort_without_dup(list1):
#     list1 = list(set(list1))
#     for i in range(len(list1)-1):
#         flag = True
#         for j in range(len(list1)-1-i):
#             if (list1[j] < list1[j+1]):
#                 list1[j], list1[j+1] = list1[j+1], list1[j]
#                 flag = False
#         if(flag):
#             return list1
#     return list1
# print(desc_sort_without_dup([5,3,5,2,1,1,7,3,5,6]))

# #  Question 10
# #  Write a Program to Remove brackets from an algebraic expression(can not use predefined function).

# def rem_brace(str):
#     new_str = ''
#     for i in str:
#         if (i not in ['(', ')']):
#             new_str+=i
#     return new_str
# print(rem_brace('a + b-(9+c)=3'))

# # Question - 11
# # Write Program to remove duplicate elements in an array and sort it in Accending order(can not use predefined function).

# def asec_without_dup(list1):
#     list1 = list(set(list1))
#     for i in range(len(list1)-1):
#         flag = True
#         for j in range(len(list1)-1-i):
#             if ord(list1[j]) > ord(list1[j+1]):
#                 list1[j] , list1[j+1] = list1[j+1], list1[j]
#                 flag = False
#         if flag:
#             return list1
#     return list1
# print(asec_without_dup(['Z', 'A', 'P', 'C', 'A', 'Z' , 'K', 'N', 'C']))

# # Question - 12
# # If subseq's  array  sequence is present in the array, returns true or else returns false.

# def check_subarray(list1, sub):
#     for i in sub:
#         if i not in list1:
#             return False
#     return True
# print(check_subarray( [5, 7, 3, 2, 2, 7,-1, 5, -3, 13, 4], [7, -1, 4, -3,303]))

# # Question - 13
# # Find sum of the Unique numbers: 

# def sum_of_uniq(list1):
#     uniq_list = []
#     sum = 0
#     for i in list1:
#         if i not in uniq_list:
#             uniq_list.append(i)
#             sum+=i
#     return sum
# print(sum_of_uniq([1, 2, 2, 1, 3, 5, 1]))








#############################################################


# Question - 8
# Question - 6
# Question - 5
# Question - 4
# Question - 1