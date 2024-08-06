#project 1
name=input("Please enter your name")
tamil=int(input("Enter your tamil mark"))
english=int(input("Enter your english mark"))
maths=int(input("Enter your maths mark"))
chemistry=int(input("Enter your chemistry mark"))
history=int(input("Enter your history mark"))
total = tamil+english+maths+chemistry+history
average=total/5
print("Name:",name)
print("Total marks:",total)
print("Average:",average)
if (average>=90 and average<=100):
    print("Grade: A grade ")
elif (average>80 and average<=90):
    print("Grade: B grade")
elif (average>70 and average<=80):
    print("Grade: C grade")
elif (average>60 and average<=70):
    print("Grade: D grade")
else:
    print("Grade: E grade")

