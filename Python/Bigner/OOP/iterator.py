fruits="abc"
# for x in fruits:
#     print(x)
myit=iter(fruits)
print(next(myit))
print(next(myit))
print(next(myit))
 

class myNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = myNumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

