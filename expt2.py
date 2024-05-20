# 5)Write a python program to check the given number is odd or even


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("The given number is  odd")
else:
   print("The given number is Odd")


# 6)Write a Python program to print the largest of two numbers.

a=int(input("enter the first  number:"))
b=int(input("enter the second number:"))
if(a>b):
      print(a ,"is the largest number")
else:
       print(b ," is the largest number")

      
   
# 7) Write a Python program to print the largest of three numbers.

    
a=int(input("enter the first  number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>b)and (a>c):
      print(a ,"is the largest number")
elif(b>a)and (b>c):
       print(b ," is the largest number")
else:
     print(c,"is the largest number")


# 8)Write a Python program to check whether a person is eligible to vote or not.
age=int(input("Enter your age:"))
if(age>=18):
     print(age,"You are eligible for voting")
else:
     print(age,"Sorry...You are not eligible for voting")

  # 9)Write a Python program to check whether the given number is positive or negative.
num=int(input("Enter a number:"))
if(num>0):
    print("number is positive")
elif(num==0):
    print("number is Zero")
else:
    print("number is negative")


 # 10)Write a Python program to display the grades according to the total marks.

mark=int(input("Please enter your total mark:"))
if(mark>=90):
      print("A+")
elif(mark>=80):
      print("B+")
elif(mark>=70):
      print("C+")
elif(mark>=60):
      print("D+")
elif(mark>=50):
      print("Pass")
else:
      print("You are failed")




 
      















     
       
