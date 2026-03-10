x=int(input("Enter student Marks"))
percentage= x/600*100
print(percentage)
if(percentage>90):
    print("grade A+")
elif(percentage<90 and percentage>85):
    print("A grade")
elif(percentage>70):
    print("Grade B")
elif(percentage>60):
    print("grade c")
elif(percentage<60):
    print("FAIL")