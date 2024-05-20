 # 11 Write a Python program to display factorial of a number.
a=int(input('Enter a number:'))
fact=1
for i in range(1,a+1):
     fact=fact*i

print(a,'!=',fact)

#12 Write a Python program to display multiplication table of given number. 

num=8
for i in range(1,11):
    print(num,'x',i,'=',num*i)

#13 Write a Python program to display(*)
    
for i in range(1,5):
    for j in range(i):
        print('*',end=' ')
    print()

#14.Write a Python program to display 1 22 333

  

    
for i in range(1,5):
    for j in range(i):
        print(i,end=' ')
    print()

#15.Write a Python program to display 1 12 123 1234
    
for i in range(1,5):
    for j in range(i):
        print(j+1,end=' ')
    print()


# 16 write a Python program to check if a given character is a vowel or not.

x = (input('Enter a variable:'))
if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
    print("vowel")
else:
    print("consonants")

#17 Write a Python program to print the sum of n natural numbers

n=int(input('Enter a number'))
sum=0
for i in range(1,n):
    sum=sum+i
print('sum of',n,'natural numbers=',sum)


#18 Write a Python program to check prime number using for loop
n=int(input('enter the number'))
i=0
c=0
for i in range(1,n+1):
     if n%1==0:
          c=c+1
          if c==2:
           p=print('it is a prime number')
     else:
                   print('it is not a prime number')
                   
                  
#19Write a Python program to display given pattern using while loop
1
12
123
1234
12345

           
     
for i in range(1,6):
    for j in range(i):
        print(j+1,end=' ')
    print()
         
          
     

          
          



    

    
