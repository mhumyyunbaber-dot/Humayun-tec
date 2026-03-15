import tkinter as tk
def calculator():
    def Add(x,y):
        return x+y
    def Sub(x,y):
        return x-y
    def Multiply(x,y):
        return x*y
    def Divide(x,y):
        if y==0:
            return "Error! not divisible" 
        return x/y
    while True:
        print("select operation")
        print("1 : Add")
        print("2 : Subtract")
        print("3 : Multipltication")
        print("4 : Divide\n5.Exit")
        choice=input("Enter a choice (1/2/3/4/5):")

        if choice=='5':
            print("Exiting Calculator,Goodbye")
            break  
        num1=float(input("Enter 1st Number:"))
        num2=float(input("Enter 2nd Number:"))

        if choice=="1":
            print("Result",Add(num1,num2))
        elif choice=="2":
            print("Result",Sub(num1,num2) )
        elif choice=="3":
            print("Result",Multiply(num1,num2))
        elif choice=="4":
            print("Result",Divide(num1,num2))
        else:
            print("invalid input")
# Now Gui code by using thinker
def thinker():
    def click(button_text):
        if button_text=="=":
            try:
                result=str(eval(entry.get()))
                entry.delete(0,tk.END)
                entry.insert(tk.END,result)
            except:
                entry.delete(0,tk.END)
                entry.insert(tk.END,"Error")
        elif button_text=="C":
            entry.delete(0,tk.END)
        else:
            entry.insert(tk.END,button_text)
        
    root=tk.Tk()
    root.title("GUI Cal")

    entry=tk.Entry(root,width=20,font=("Arial",18))
    entry.grid(row=0,column=0,columnspan=4)

    buttons=[
        "7","8","9","/",
        "4","5","6","*",
        "1","2","3","-",
        "0",".","=","+",
        "C"
    ]

    row,col=1,0
    for b in buttons:
        btn = tk.Button(root,text=b,width=5,height=2,font=("Arial",14),
             command=lambda x=b: click(x))
        btn.grid(row=row,column=col)
        col+=1
        if col>3:
            col=0
            row+=1
    root.mainloop()

thinker()
