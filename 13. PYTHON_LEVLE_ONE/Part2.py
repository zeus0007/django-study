# STRINGS

# Basics
'hello'
"hello"

"I'm a dog"

mystring = 'abcdefg'
print(mystring[0])
print(mystring[-1])

# slice
print(mystring[2:])
print(mystring[2:5])
print(mystring[::2])  # aceg
x = mystring.upper()  # 대문자 만들기 소문자는 lower
# 함수를 쓰기 전에 .만 써서 쓸 수 있는 종류를 보고 모르는것은 검색해보면 된다.
x = mystring.capitalize()
x = mystring.split('o')  # list형으로 바뀌고 인자 값으로 잘라낼때 기준으로 삼을 값을 넣어준다.
print(mystring)  # 함수를 적용해도 원래 값은 안바뀜
print(x)

x = "Insert another string here: {}".format("INSERT ME!")
# format을 쓰면 {}안에 원하는 값을 넣을 수 있다.
# 두개이상 넣기
x = "Item One: {} Item Two: {}".format("dog", "cat")
# 변수를 사용해서 넣기
x = "Item One: {x} Item Two: {y}".format(x="dog", y="cat")

print(x)
