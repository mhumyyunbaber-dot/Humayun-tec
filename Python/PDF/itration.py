for x in range(0,13):
    print(x)

fruits=["apple","tie","vanila"]

for i in fruits:
    print("i like this",i)

count=1
while count<=5:
    print("count is",count)
    count +=1

class Mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 5:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass=Mynumber()
for n in myclass:
    print(n)

name=["ali","humayun","jahanzaib"]
for index,name in enumerate(name):
    print(index,name)

for x in range(1,21):
    print(x)

count=10
while count >=1:
    print(count)
    count -=1


count=1
while count >=7:
    print(count)

class Mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=5:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=Mynumber()
for n in myclass:
    print(n) 

