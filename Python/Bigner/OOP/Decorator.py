def greet(fx):
    def mfx(*arg,**kwargs):
        print("Good Morning")
        fx(*arg,**kwargs)
        print("Thanks for using this function")
    return mfx
@greet
def Hello():
    print("Hello World")
def add(a,b):
    print(a+b)


Hello()
greet(add)(1,4)    