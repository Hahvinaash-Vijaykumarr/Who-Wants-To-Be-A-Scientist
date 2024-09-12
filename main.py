# HI GUYSSSSS!! thanks for doing the documentation, the comments in # are the explanations
# (or at least attempted explanations) of what the code means. if yall any questions, js tele
# me okay!!!!!!! miss yall

from time import sleep # suspends (waits) execution of the current thread for a given number of seconds
from random import randint
import testqs # import the question bank and ascii art, a separate file
#import ascii_art

#these are all global variables
status = "on"
score = 0
help_score = 2
# helpers is a list
helpers = ["A) The 50/50", "B) The Class Vote", "C) The Teacher"]
#print(ascii_art.logo)

#first function: asking the questions
def ask_question(question, answers, correct, amount, audience, teacher_hint):
  print(question)
  sleep(3)
  for answer in answers:
    print(answer)
    sleep(1)
  user_answer = input("What is your answer?(A-D or H for helper) ")
  if user_answer.upper() == "H": #.upper() makes the input capital letters
    use_helper(correct, amount, audience, teacher_hint)
  elif user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(0.2)        
  else: # helpers
    global help_score # We can only access the global variable but cannot modify it from inside the function. Therefore, 'global' keyword is used
    if help_score > 0:
      help()
      for answer in answers:
        print(answer)
        sleep(1)
      user_answer2 = input("What is your answer?(A-D or H for helper) ")
      if user_answer2.upper() == "H":
        use_helper(correct, amount, audience, teacher_hint)
      elif user_answer2.upper() == correct:
        print(" ")
        correct_answer(amount)
        sleep(0.2)
      else:
        print(" ")
        game_over() # an exit function
    else:
      print(" ")
      game_over()

# When user answers the correct question, this function would be displayed
def correct_answer(amount):
  sleep(1)
  print("That is...")
  sleep(1)
  print("CORRECT!!")
  print(" ")
  sleep(1)
  print("*applause*")  
  global score
  score += amount
  print(" ")
  sleep(1)
  print(f"Very well done {name}, your current score is {score}!")
  print(" ")
  sleep(1)

# Helper function: checks if there are any helpers left, 
# and if there are helpers left: when it's called, 
# we remove the helper from the list
def use_helper(correct, amount, audience, teacher_hint):
  print(" ")  
  global helpers
  if len(helpers) == 0: 
# when the length of the list of the helpers is 0, 
# indicating no more helpers left as we remove 
# the helpers each time it's called
    print("Sorry, you have no helpers left!")
    sleep(0.2)
    user_answer = input("What is your answer? ") # a second chance to answer
    if user_answer.upper() == correct: 
      print(" ")
      correct_answer(amount)
      sleep(0.2)
    else: # no chances given if they answer wrongly
      print(" ")
      game_over()    
  else:    
    print("You have the following helpers:")
    sleep(0.2)
    for helper in helpers:
      print(f"{helper}-Helper")
      sleep(1)
    helper_selection = input("Which helper would you like to use?")
    if helper_selection.upper() == "A":
      helpers.remove("A) The 50/50") 
# .remove() takes one element as an argument and removes it from the list
      helperA(correct, amount)
    elif helper_selection.upper() == "B":
      helpers.remove("B) The Class Vote")
      helperB(correct, amount, audience)
    elif helper_selection.upper() == "C":
      helpers.remove("C) The Teacher")
      helperC(correct, amount, teacher_hint)

# Function for the first helper: 50/50
# to create 50/50:
# generates a new list with correct answer, and adds a random option.
# Thus, 50-50 is generated. 
def helperA(correct, amount):
  answers = ["A", "B", "C", "D"]
  helper_answer = [correct]  # creates new list with the correct answer
  answers.remove(correct) # remove the correct answer, so that can randomize
  number = randint(0, 2) # return a number between 0 & 2 
  helper_answer.append(answers[number]) # adds 1 wrong ans to helper_ans list
  helper_answer.sort() # orders items of the helper_ans list in ascending order
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)  
  print(f"The remaining answers are {helper_answer[0]} and {helper_answer[1]}")
  sleep(3)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(0.2)
  else:
    print(" ")
    game_over()

def helperB(correct, amount, audience): # the  class vote
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)
  print(f"The class vote is: {audience}") # refer to audience(class) percentages for each answer
  sleep(3)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(0.2)
  else:
    print(" ")
    game_over()

def helperC(correct, amount, teacher_hint): # The Teacher
  sleep(1)
  print(".")
  sleep(1)
  print("..")
  sleep(1)
  print("...")
  sleep(1)
  print("Here is what your Teacher said:")
  sleep(1.5)
  print(teacher_hint)
  sleep(3)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(0.2)
  else:
    print(" ")
    game_over()

def help():
  global help_score
  help_score -= 1
  sleep(1.5)
  print(" ")
  print("...are you SURE that is correct?")
  sleep(0.2)
  print("again the possibilities are:")
  sleep(0.2)    

def game_over():
  global status
  status = "off"
  print("That is...")
  sleep(1)
  print("wrong!")
  print(" ")
  sleep(1)
  print(f"sorry {name}, you lost!")
  print(" ")
  print(" ")
  sleep(1)
  print("GAME OVER!")


# START OF THEATRICS (wtv will be displayed)
print(" ")
print(" ")
print(" ")  
print("Ladies and Gentlemen!")
print(" ")
sleep(1.3)
print("Welcome to a new round of")
print(" ")
sleep(0.7)
print("WHO")
sleep(0.7)
print("WANTS")
sleep(0.7)
print("TO")
sleep(0.7)
print("BE")
sleep(0.7)
print("A")
sleep(0.7)
print("SCIENTIST?!")
print(" ")
sleep(1.3)
print("*applause*")
print(" ")
sleep(0.025)

print("OUR FIRST CANDIDATE TONIGHT IS ....")
sleep(1.5)
print("...ehm...")
print(" ")
sleep(1.5)
name = input("sorry, I forgot your name. What is your name? (enter your name) ")
print("Of course that is your name!")
print(" ")
sleep(1.5)
print(f"Everyone, a BIG ROUND OF APPLAUSE FOR OUR CANDIDATE {name.upper()}!")
print(" ")
sleep(0.2)
print("*big round of applause*")
print(" ")
sleep(0.2)

print("ok, let's get started. First a reminder, you have 3 helpers:")
sleep(0.2)
for helper in helpers:
  print(f"{helper}-Helper")
  sleep(1.5)
print("You can only use ONE helper for each question.")
sleep(0.025)
print(" ")
print(" ")
print("OK, let's go!")
print(" ")
print(" ")
sleep(1.5)

# IMPROVE: Make it into a loop
#def questions():
#  for i in range(0,2):
#    q = testqs.getQuestion(0)
#    if status == "on":
#         ask_question(q[0], q[1], q[2], q[3], q[4], q[5])

def Questions():
  for i in range(len(testqs.question_bank)):
    q = testqs.getQuestion(i)
    if status == 'on':
      ask_question(q[0], q[1], q[2], q[3], q[4], q[5])

Questions()

'''

q = testqs.getQuestion(0)
if status == "on":
  ask_question(q[0], q[1], q[2], q[3], q[4], q[5])
q = testqs.getQuestion(1)
if status == "on":
  ask_question(q[0], q[1], q[2], q[3], q[4], q[5])
q = testqs.getQuestion(2)
if status == "on":
  ask_question(q[0], q[1], q[2], q[3], q[4], q[5])
'''

if status == "on":
  print("CONGRATULAAAAAAAAAAAAATIONS!!!!!!")
  sleep(0.2)
  print(" ")
  print(f"YOUR SCORE IS {score}!!")
  sleep(0.2)
  print(" ")
  print("YOU ARE THE WINNER")
  sleep(0.2)
  print(" ")
#  print(ascii_art.medal)
  sleep(0.2)
  print("OUR LATEST MEMBER IN THE ALL TIME HALL OF FAME...")
  print(" ")
  sleep(3)
  print("IS...")
  print(" ")
  sleep(1.5)
  print("THE UNFORGETABLE BRILLIANT SCIENTIST: ")
  print(" ")
  sleep(3)
  print(f"{name.upper()}!!!")
  sleep(1.5)
  print("*incredibly loud applause and cheering*")
  sleep(1.5)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print("   ...")
  sleep(3)
  print(" ")
  print(" ")
  print(" ")
  print("THE END")
