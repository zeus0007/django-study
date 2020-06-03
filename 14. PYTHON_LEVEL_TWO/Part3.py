# class Dog():

#     # CLASS OBJECT ATTRIBUTE
#     species = "mammal"

#     # init은 method임 내장 method
#     def __init__(self, breed, name):  # 여기서 breed,name이 attribute임
#         self.breed = breed
#         self.name = name


# #mydog = Dog(breed="Lab", name="Sammy")
# mydog = Dog("Lab", "Sammy")
# #otherdog = Dog(breed="Huskie")
# print(mydog.breed)
# print(mydog.name)

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
# radius를 바꾸는 방법
# 1
myc.radius = 100
# 2 2번의 방식의 프로그래밍도 활용할줄 알아야한다.
myc.set_radius(100)
print(myc.radius)
print(myc.area())
