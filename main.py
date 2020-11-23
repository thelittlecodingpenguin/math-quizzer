import random
from os import system as o
import time

CRED    = '\33[31m'
CGREEN  = '\33[32m'
CWHITE  = '\33[37m'
print(CWHITE)

lvl1 = input("Level min: ").strip()
lvl2 = input("Level max: ").strip()
rounds = input("How many rounds do you want to do? ").strip()

rounds = float(rounds)
lvl1 = float(lvl1)
lvl2 = float(lvl2)

counter = 0
num1 = random.randint(round(lvl1), round(lvl2))
num2 = random.randint(round(lvl1), round(lvl2))

score = 0
eq = ["+", "/", "-", "*", "%", "^"]

def format_equation(e, question1, question2):
    print("  " + str(question1))
    print(e)
    print("  " + str(question2))
    print("--------")

def check_times(question, question1, user_answer):
    answer = question * question1
    if user_answer == answer:
        print(CGREEN + "Correct")
        print(CWHITE)
        return True
    else:
        print(CRED + "Incorrect")
        print(CWHITE)
        return False

def check_division(question, question1, user_answer):
    answer = question / question1
    if user_answer == answer:
        print(CGREEN + "Correct")
        print(CWHITE)
        return True
    else:
        print(CRED + "Incorrect")
        print(CWHITE)
        return False


def check_minus(question, question1, user_answer):
    answer = question - question1
    if user_answer == answer:
        print(CGREEN + "Correct")
        print(CWHITE)
        return True
    else:
        print(CRED + "Incorrect")
        print(CWHITE)
        return False

def check_addition(question, question1, user_answer):
    answer = question + question1
    if user_answer == answer:
        print(CGREEN + "Correct")
        print(CWHITE)
        return True
    else:
        print(CRED + "Incorrect")
        print(CWHITE)
        return False


def check_modulo(question, question1, user_answer):
    answer = question % question1
    if user_answer == answer:
        print(CGREEN + "Correct")
        print(CWHITE)
        return True        
    else:
        print(CRED + "Incorrect")
        print(CWHITE)
        return False

def check_pow(question, question1, user_answer):
    answer = question ** question1
    if user_answer == answer:
        print(CGREEN + "Correct")
        print(CWHITE)
        return True
    else:
        print(CRED + "Incorrect")
        print(CWHITE)
        return False

while counter < round(rounds):
    e = random.choice(eq)
    format_equation(e, num1, num2)
    answer = input("> ").strip().lower()
    if str(answer) == "q":
        break
    answer = float(answer)
    if e == "+":
        if check_addition(num1, num2, answer) == True:
            score += 1
            print(f"Score: {score}")
    elif e == "%":
        if check_modulo(num1, num2, answer) == True:
            score += 1
            print(f"Score: {score}")
    elif e == "-":
        if check_minus(num1, num2, answer) == True:
            score += 1
            print(f"Score: {score}")
    elif e == "*":
        if check_times(num1, num2, answer) == True:
            score += 1
            print(f"Score: {score}")
    elif e == "/":
        if check_division(num1, num2, answer) == True:
            score += 1
            print(f"Score: {score}")
    elif e == "^":
        if check_pow(num1, num2, answer) == True:
            score += 1
            print(f"Score: {score}")
        
    num1 = random.randint(round(lvl1), round(lvl2))
    num2 = random.randint(round(lvl1), round(lvl2))
    counter += 1
    time.sleep(1)
    o("clear")

print("Your final score is " + str(score) + "!")
