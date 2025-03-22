from random import randint
import time
name=input("What is you name: ")
number=randint(1,100)
def introduction():
    print("Hello,",name,"we are playing guessing number game from 1 to 100")
    print("I am thinking")
    if number%2==0:
        print("This number is even")
    else:
        print("This number is odd")
    time.sleep(2)
    print("Go ahead write you guess!")
def checking():
    guesstimes=0
    while guesstimes<7:
        try:
            guess=int(input("Guess: "))
            if guess==number:
                print("True")
                break
            elif guess<number:
                print("The number that you have entered is to low!")
            else:
                print("The number that you have entered is too high!")
            guesstimes+=1
        except NameError:
            print("You can't enter like that")
        except ZeroDivisionError:
            print("You can't enter like that")
        except SyntaxError:
            print("You can't enter like that")
        except ValueError:
            print("You can't enter like that")
        guesstimes+=1
    if guesstimes>5:
        print("You can't guess!")
playagain="yes"
while playagain.lower()=="yes":
    introduction()
    checking()
    playagain=input("Do you want to play again: ")
    if playagain.lower()=="no":
        break
print("Goodbye")
exit()
    
    
    
    
    
    
    
