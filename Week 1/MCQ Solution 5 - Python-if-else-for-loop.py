import os
import time

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
class color:
    RED='\033[31m'
    ENDC='\033[m'
    GREEN='\033[32m'

score=0
screen_clear()
print("1).What will the following code print out?\n[\n  x = 0\n  if x<2:\n     print('Small')\n  elif x<10:\n     print('Medium')\n  else:\n     print('LARGE')\n  print('All done')\n]\nA. Small \nB. Medium\n   All done\nC. Small\n   Medium\n   LARGE\nD. Small\n   All Done")
ans=input("Enter your Choice:")
screen_clear()
if ans=="d" or ans=="D":
    score+=1
    print(color.GREEN+"Correct Choice")
    print("Correct.Current Score:",score,"out of 5"+color.ENDC)
else:
    print(color.RED+"Wrong/Invalid Choice.Correct Option is A")
    print("Current Score:",score,"out of 5"+color.ENDC)
time.sleep(1)
print("2) What will the following code will print out?\n[\nfor num in range(-2,5,3):\n   print(num)\n]\nA. -2 -3 -5\nB. -2  1  4\nC. -2 -1  0\nD. -2 -1  5")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B":
    score+=1
    print(color.GREEN+"Correct Choice")
    print("Correct.Current Score:",score,"out of 5"+color.ENDC)

else:
    print(color.RED+"Wrong/Invalid Choice.\n")
    print("Current Score:",score,"out of 5"+color.ENDC)
time.sleep(1)
print("3) What is the value of x after the following nested for loop completes its execution?\n[\nx=0\nfor i in range(10:\n  for j in range(-1,-10,-1):\n      x+=1\nprint(x)\n]\nA. 100\nB. 90\nC. 99\nD. 9")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B":
    score+=1
    print(color.GREEN+"Correct Choice")
    print("Correct.Current Score:",score,"out of 5"+color.ENDC)
else:
    print(color.RED+"Wrong/Invalid Choice.Correct Option is B")
    print("Current Score:",score,"out of 5"+color.ENDC)
time.sleep(1)
print("4) Which of the following is a valid for loop in Python?\nA. for(i=0; i < n; i++)\nB. for i in range(0,10,4):\nC. for i in range(0,5)\nD. for i in range(5):")
ans=input("Enter your Choice:")
screen_clear()
if ans=="d" or ans=="D"or ans=="b"or ans=="B":
    score+=1
    print(color.GREEN+"Correct Choice")
    print("Correct.Current Score:",score,"out of 5"+color.ENDC)
else:
    print(color.RED+"Wrong/Invalid Choice.Correct Option is D")
    print("Current Score:",score,"out of 5"+color.ENDC)
time.sleep(1)
print("5) When does the else statement written after loop executes?\nA. When break statement is executed in the loop.\nB. When loop condition becomes false.\nC. Else statement is always executed.\nD. None of the above.")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B":
    score+=1
    print(color.GREEN+"Correct Choice")
    print("Correct.Current Score:",score,"out of 5"+color.ENDC)
else:
    print(color.RED+"Wrong/Invalid Choice.Correct Option is A")
    print("Your Total Score is:",score,"out of 5"+color.ENDC)
if (score>=3):
    print(color.GREEN+"Congratulation! You secured",(score/5)*100,"%.")
else:
    print(color.RED+"You secured",(score/5)*100,"%. You need more practice."+color.ENDC)

time.sleep(5)
