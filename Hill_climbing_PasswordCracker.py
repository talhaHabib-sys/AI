#Talha Habib
# roll no: 17B-048-CS
#SecB
#TASK-2
import random
import string as stn
import getpass
def random_sol(length=10):
    return[random.choice(stn.printable) for _ in range(length)]
    
def User_input():
    targ=getpass.getpass("Enter passowrd of 10 digits:\n")
    return targ


def eval(solve):
 difrence=0
 for i in range(len(targ)):
    s_l=solve[i]
    t_g=targ[i]
    difrence+=abs(ord(s_l)-ord(t_g))
 return difrence
def muta_tion(solve):
        ind=random.randint(0,len(solve)-1)
        solve[ind]=random.choice(stn.printable)

perfect=random_sol()
targ=User_input()
if ((len(targ)>10) | (len(targ)<10)):
    print("Your passowrd length is greater than 10 or less than 10 enter Passowrd of 10 digits Only!")
    input()
else:
    marks=eval(perfect)

    while True:
        print("solution",perfect,"Score:",marks)
        if marks==0:
            print(perfect)
            input()
            break

        newsolve = list(perfect,)
        muta_tion(newsolve)
        perfect_marks=eval(newsolve)
        if perfect_marks<marks:
            marks=perfect_marks
            perfect=newsolve
