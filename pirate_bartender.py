import random

def askQuestion():
  questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
  }

  answers = {}

  for key in questions.keys():
    my_input = raw_input(questions[key])
    if my_input == "yes" or my_input == "y":
      answers[key] = True
    else:
      answers[key] = False
  return answers

def makeDrink(theAnswers):
  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
  }
  theDrink = []
  for key in theAnswers:
    if theAnswers[key] == True:
      theDrink.append(random.choice(ingredients[key]))
  return theDrink

if __name__ == '__main__':
  print makeDrink(askQuestion())

