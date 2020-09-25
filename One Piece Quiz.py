# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Creating a Header
def header():

  print("One Piece Quiz")

  username = input("\nPlease enter your name: ").title()
  print(username)

header()

#Quiz items
def quiz():
  score1 = 0
  ques1 = input("Which pirates is Tama waiting for?:\n(A) Buggy\n(B) Ace\n(C) Zoro\n(D) Roger\n\n")
  if ques1 == 'B':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques2 = input("\nWhich is the main means of communication in One Piece world?\n(A) Phone Shells\n(B) News Coos\n(C) Telegram Beetles\n(D) Transponder Snails\n\n")
  if ques2 == 'D':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques3 = input("\nWho created athe poisonous gas, Koro?\n(A) Avelon\n(B) Vergo\n(C) Caesar\n(D) Jack\n\n")
  if ques3 == 'C':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques4 = input("\nWhat color is Ichiji's raid suit?\n(A) Yellow\n(B) Red\n(C) Pink\n(D) Green\n\n")
  if ques4 == 'B':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques5 = input("\nHow many swords does Zoro wield when activating Toro, Ootoro and Salmon?\n(A) Three\n(B) Nine\n(C) One\n(D) Two\n\n")
  if ques5 == 'D':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques6 = input("\nWho does Law name as the strongest creature in the world?\n(A) Blackbeard\n(B) Big Mom\n(C) Kaido\n(D) Shanks\n\n")
  if ques6 == 'C':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques7 = input("\nWho was in the picture frame that made Big Mom devastated when it was broken?\n(A) Katakuri\n(B) Kaido\n(C) Mother Caramel\n(D) Lola\n\n")
  if ques7 == 'C':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques8 = input("\nWhat tattoo did Nami have, before the one she has currently?\n(A) Arlong's Mark\n(B) Tangerine Trees\n(C) Pinwheels\n(D) Money\n\n")
  if ques8 == 'A':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques9 = input("\nWhat pirate crews were Shanks and Buggy both members of when they were younger?\n(A) Cook Pirates\n(B) Whitebeard Pirates\n(C) Roger Pirates\n(D) Rumbar Pirates\n\n")
  if ques9 == 'C':
    print("Correct")
    score1+=1
  else:
    print("Wrong")
  ques10 = input("\nWhat part of the ocean is the island Amazon Lily located on?\n(A) Calm Belt\n(B) Grand Line\n(C) West Blue\n(D) North Blue\n\n")
  if ques10 == 'A':
    print("Correct\n")
    score1+=1
  else:
    print("Wrong\n")

  #This function is created to check your score
  final_score = (score1 / 10) * 100

  if final_score > 70:
    print("Congratulations! Your final score is: ", int(final_score),"%.\n\nYou are a certified One Piece Fan.")
  else:
    print("Your final score is: ", int(final_score),"%. Try again next time!\n\nBetter refresh and watch it again.")

quiz()
