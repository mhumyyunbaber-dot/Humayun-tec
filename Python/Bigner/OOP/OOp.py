class person:
    def __init__(self,n,o):
        print("Hey I am a Person")
        self.name=n
        self.occ=o 
    def info(self):
        print(f"{self.name}  is learning  {self.occ}")
a=person("Humayun", "develpor")
b=person("Bisma","HR")
c=person(1,2)
a.info()
b.info()
c.info()