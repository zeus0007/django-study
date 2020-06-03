# INHERITANCE 상속
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self) #주석처리해도 상속은 잘된다.
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")


mydog = Dog()
mydog.whoAmI()
mydog.eat()

# SPECIAL METHODS


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {},Autor:{},Pages:{}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")


b = Book("Python", 'jose', 200)
print(b)
len(b)
del(b)
