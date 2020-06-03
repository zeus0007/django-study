# x = 25


# def my_func():
#     x = 50
#     return x


# print(x)#25
# my_func()
# print(x)#25 지역에서 변경한것은 적용되지 않음

# # LOCAL
# lambda x: x**2

# # Enclosing function Locals
# name = 'This is a global name!'


# def greet():
#     name = "sammy"

#     def hello():
#         print("hello " + name)

#     hello()


# greet()
# print(name)

# Built-In
# len = 23#not work
#########################################################
x = 50


def func():
    # print('x is:', x)
    # x = 1000
    # print('local x changed to :', x)

    # global x
    x = 1000
    return x


print('before function call, x is:', x)
x = func()
print('after function call, x is:', x)
