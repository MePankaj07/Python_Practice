# Problem 1 : Write a program to find the greatest of four numbers entered by the user?
# a=int(input("Enter Number 1 : "))
# b=int(input("Enter Number 2 : "))
# c=int(input("Enter Number 3 : "))
# d=int(input("Enter Number 4 : "))
# if(a>b):
#     f1=a
# else:
#     f1=b
# if(c>d):
#     f2=c
# else:
#     f2=d
# if(f1>f2):
#     print(f1)
# else:
#     print(f2)

# Problem 2: Write a program to find out whether the stundent is pass or fail,
#  if it requires 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from user?

# Maths = int(input("Enter marks for Maths out of 100 : "))
# English = int(input("Enter marks for English out of 100 : "))
# Physics = int(input("Enter marks for Physics out of 100 : "))
# totalMarks = Maths + English + Physics
# percentage = totalMarks/300*100
# if(Maths<33 or English<33 or Physics<33):
#     print("You are Failed due to less than 33 percent marks in one of the subject.")
# elif(percentage<40):
#     print("You are Failed, Due to less Total Percentage.")
# else:
#     print("Congratulations!, You passed the Exam.")

# Problem 3: A spam comment is defined as a text containing following keywords :
# "make a lot of money", "follow now", "subscribe this", "click this".
# write a program to detect these spams

# CmntSpam = ["make a lot of money", "follow now", "subscribe this", "click this"] 
# Cmnt = input("Enter Your Comment : ")

# if(Cmnt in CmntSpam):
#     print("Error For Spam!")
# else:
#     print(Cmnt)

# Problem 4: Write a program to find whether the given username lenght is greater than 10 characters or not?

# userName = input("Enter Your Name : ")
# if(len(userName)>10):
#     print("Length is greater than 10.")
# else:
#     print("Lenght is less than 10.")

# Problem 5: Write a program to find whether the person is talking about harry or not?

# post = input("Enter a Name  :  ")

# PreDefined = "Harry"

# if (post.capitalize()==PreDefined):
#     print("Person is talking about Harry.")
# else:
#     print("Person is not talking about Harry.")
