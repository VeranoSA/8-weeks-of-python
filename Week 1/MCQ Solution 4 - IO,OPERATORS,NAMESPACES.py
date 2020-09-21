import os
import time

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


score=0
screen_clear()
print("1) Which of the following is not a valid namespace?\nA. Global namespace\nB. Public namespace\nC. Built-in namespace\nD. Local namespace")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is B")
    print("Current Score:",score,"out of 5")

print("2) Which of the following is false about “from-import” form of import?\nA. The syntax is: from module  name import identifier\nB. This form of import prevents name clash\nC. The namespace of imported module becomes part of importing module\nD. The identifiers in module are accessed directly as: identifier")
ans=input("Enter your Choice:")
screen_clear()
if ans=="a" or ans=="A":
    score+=1
    print("Correct.\nCurrent Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is A")
    print("Current Score:",score,"out of 5")

print("3) Which is the correct operator for power(xy)?\nA. X^y\nB. X**y\nC. X^^y\nD. None of the Above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is B")
    print("Current Score:",score,"out of 5")

print("4) What is the order of precedence in python? \ni) Parentheses \nii) Exponential \niii) Multiplication \niv) Division \nv) Addition \nvi) Subtraction?\nA. i,ii,iii,iv,v,vi \nB. ii,i,iii,iv,v,vi\nC. ii,i,iv,iii,v,vi \nD. i,ii,iii,iv,vi,v")
ans=input("Enter your Choice:")
screen_clear()
if ans=="a" or ans=="A":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is A")
    print("Current Score:",score,"out of 5")

print("5) What is the output of the following print() function \nprint('%d %d %.2f' % (11, '22', 11.22))?\nA. 11 22 11.22\nB. TypeError\nC. 11 ‘22’ 11.22")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B":
    score+=1
    print("Correct.Your Total Score is:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is B")
    print("Your Total Score is:",score,"out of 5")
if (score>=3):
    print("Congratulation! You secured",(score/5)*100,"%.")
else:
    print("You secured",(score/5)*100,"%. You need more practice.")

time.sleep(10)
