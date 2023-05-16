# this is a comment = will not be interpreted


"""
 multiline 
 comment
"""

# ! Variables :

# var studentName = "Steve"

student_name = "Steve"

# numbers :

age = 39  # - Integer

rate = 3.14  # -Float


# console.log(age)

# print(age)

# print("My name is " + student_name + " my age is " + age)

# print(f"My name is {student_name} my age is {age}")

# Boolean

vote = True
is_admin = False
is_valid = None

#          0-1-2- 3
my_list = [10, 1, -2, 45]
# print(my_list[2])
# my_list[2] = "change"
# print(my_list[2])

# .push

# my_list.append("push")

# print(my_list)

# my_list.pop()
# print(my_list)

my_list.sort()
# print(my_list)

# objects

# dictionaries in PY

student_dic = {"name": "Tom", "age": 55}

student_dic["name"] = "Michael Jordan"

# tupples

# list immutables ? --- cannot be change

tup = (1, 2, 3)
student_dic['age'] = tup

# tup.append("444")
# print(student_dic)


# condition

# if(true == false){

# }

# if 5 == 5:
#     print("hello")


# Loops
"""
    for(var i = 1 ; i < 10 ; i++){
    
    }
    
    """

# for i in range(1, 10):
#     print(i)
# x = 5

# while x > 0:
#     print("hello")
#     x -= 1


superheroes = ["superman", "batman", "spiderMan", "thor", "wonder woman"]

# for i in range(len(superheroes)):
#     if superheroes[i] == "spiderMan":
#         print("petter parker")
#     else:
#         print("ay 7aja")


# Function

# function nameOftheFunction(){
# }

# def name_of_theFunction(name):
#     return name
#     print(name)


# print(name_of_theFunction("Alex"))


def multiply(*args):
    print(args)
    a = 1
    for i in args:
        a = a*i
        print(a)
    print(a)
    return (a)


multiply(5, 9)
